from site_parsing.data.orm import Offer, OfferGroup, Site
from ._parser import SiteParser
import requests
from datetime import datetime
from bs4 import BeautifulSoup

class EDFParser(SiteParser):

    site: Site = Site.get_by_id(8)
    url: str = site.url

    def get_offers(self, filters: dict = {}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        states = (state.replace('-', '')+self.departement_from_nom(state)['code'] for state in filter.get("state", ()))
                
        # Get all possible combinantions of filters with keywords and states
        filters_combinations = []
        for state in states:
            for keyword in keywords:
                filters_combinations.append(f"?search[location]=_TS_CO_Department_{state}&search[profil][34950]=34950&search[keyword]={keyword}")
            
        job_offers = []    
        for combination in filters_combinations:
            url = self.url + combination
            
            headers = {
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://www.edf.fr",
                "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
                "referer": url
            }
            response = requests.get(url, headers=headers, timeout=10)
            data = response.text

            soup = BeautifulSoup(data, 'html.parser')
            
            months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

            for offer in soup.select('.offer'):
                title = offer.select_one('.offer-description h3').text.strip()
                url = "https://www.edf.fr" + offer.select_one('.offer-link')['href']

                date_str = offer.select_one('.offer-date').text.strip()
                day, month, year = date_str.split()
                month_index = months.index(month) + 1
                date_publication = datetime.strptime(f"{day} {month_index} {year}", '%d %m %Y').date()
                
                location = offer.select('.offer-description .offer-detail-description')[1].text.strip()
                job_id = url.split('/')[-1]

                offer = Offer(
                    site=self.site,
                    title=title,
                    description=None,
                    url=url,
                    date_publication=date_publication,
                    location=location,
                    job_id=job_id,
                    offer_group=offer_group
                )
                
                if not offer.exists():
                    job_offers.append(offer)
                    
        return job_offers

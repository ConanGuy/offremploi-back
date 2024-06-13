from site_parsing.data.orm import Offer, OfferGroup, Site

from ._parser import SiteParser

from bs4 import BeautifulSoup, ResultSet
from datetime import datetime

class SafranParser(SiteParser):
    
    site: Site = Site.get_by_id(0)
    url: str = site.url
    
    def get_offers(self, filters: dict = {}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        states = filter.get("state", ())
        
        if offer_group_id != 0:
            return []
        
        driver = self.driver
        
        driver.get(self.url)
        driver.implicitly_wait(5)
        html_content = driver.page_source
        driver.quit()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        offers: list[ResultSet] = soup.find_all('div', class_='c-offer-item js-block-link')

        job_offers: list[Offer] = []
        offer: ResultSet
        for offer in offers:
            title = offer.find('a', class_='c-offer-item__title js-block-link--href').text.strip()
            link = offer.find('a', class_='c-offer-item__title js-block-link--href')['href']
            date = offer.find('span', class_='c-offer-item__date').text.strip()
            company = offer.find('span', class_='c-offer-item__infos__item').text.strip()
            location = offer.find('span', class_='icon-location').parent.text.strip()
            status = offer.find('span', class_='icon-status').parent.text.strip()
            contract = offer.find('span', class_='icon-file1').parent.text.strip()
            domain = offer.find('span', class_='icon-tags').parent.text.strip()

            offer_ = Offer(
                site = Site.get_by_id(0),
                title = title,
                description = None,
                url = link,
                date_publication = datetime.strptime(date, "%d.%m.%Y").date(),
                location = location,
                job_id = link.split("-")[-1],
                offer_group = offer_group,
            )
            
            if not offer_.exists():
                job_offers.append(offer_)
                
        return job_offers
        

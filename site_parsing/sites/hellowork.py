from site_parsing.data.orm import Offer, OfferGroup, Site

from ._parser import SiteParser

from bs4 import BeautifulSoup, ResultSet
from datetime import date

class HelloWorkParser(SiteParser):
    
    site: Site = Site.get_by_id(12)
    url: str = site.url
    
    def get_offers(self, filters: dict = {}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        states = filter.get("state", ())
        
        possible_combinations = []
        for keyword in keywords:
            for state in states:
                possible_combinations.append({"keyword": keyword, "state": state})
        
        job_offers: list[Offer] = []
        for combination in possible_combinations:
            
            keyword = combination["keyword"]
            state = combination["state"]
            
            driver = self.driver
            
            driver.get(self.url.replace("[keyword]", keyword).replace("[state]", state))
            # driver.implicitly_wait(5)
            html_content = driver.page_source
            driver.quit()

            soup = BeautifulSoup(html_content, 'html.parser')
            offers = soup.find_all("div", {'data-cy': "serpCard"})
            for offer in offers[:20]:
                header = offer.find('header')
                link_element = header.find('a', {"data-cy": "offerTitle"})
                title = link_element.get_text(strip=True)
                link = "https://www.hellowork.com" + link_element['href']
                company = offer.find('p', class_='tw-typo-s').get_text(strip=True)
                
                location = offer.find('div', {'data-cy': 'localisationCard'}).get_text(strip=True)
                contract_type = offer.find('div', {'data-cy': 'contractCard'}).get_text(strip=True)
                
                offer_ = Offer(
                    site = self.site,
                    title = title,
                    description = company,
                    url = link,
                    date_publication = date.today(),
                    location = location,
                    job_id = link.split("/")[-1].split("0")[0],
                    offer_group = offer_group,
                )
                
                if not offer_.exists():
                    job_offers.append(offer_)
                
        return job_offers
        

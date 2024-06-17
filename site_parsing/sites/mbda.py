from site_parsing.data.orm import Offer, OfferGroup, Site

from ._parser import SiteParser

from bs4 import BeautifulSoup

class MBDAParser(SiteParser):
    
    site: Site = Site.get_by_id(1)
    url: str = site.url
    
    def get_offers(self, filters: dict = {}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        states = filter.get("state", ())
        
        if "Hauts-de-Seine" not in states:
            return []
            
        job_offers = []
        for keyword in keywords:
            driver = self.driver
            
            driver.get(self.url.replace("[keyword]", keyword))
            # driver.implicitly_wait(5)
            html_content = driver.page_source
            driver.quit()
            
            soup = BeautifulSoup(html_content, 'html.parser')

            # Trouver toutes les offers d'emploi
            offers = soup.find_all('li', class_='jobs-list__results-list-item')


            for offer in offers:
                title_element = offer.find('a')
                title = title_element.text.strip()
                link = title_element['href']
                contract = offer.find('p', class_='jobs-list__results-list-item-contract').text.strip()
                location = offer.find('p', class_='jobs-list__results-list-item-localisation').text.strip()
                domain = offer.find('p', class_='jobs-list__results-list-item-domain').text.strip()

                offer = Offer(
                    site = self.site,
                    title = title,
                    description = None,
                    url = link,
                    date_publication = None,
                    location = location,
                    job_id = None,
                    offer_group = offer_group,
                )

                if not offer.exists():
                    job_offers.append(offer)
                
            return job_offers
        
if __name__ == "__main__":
    print(MBDAParser().compare_offers())
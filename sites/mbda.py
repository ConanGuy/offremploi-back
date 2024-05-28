from data.orm import Offer
from data.orm import Site

from ._parser import SiteParser

from bs4 import BeautifulSoup, ResultSet
from datetime import datetime

class MBDAParser(SiteParser):
    
    url: str = "https://www.mbda-systems.com/offers-emploi/?_job_site=le-plessis-robinson-92&_job_contract=cdi&_job_general_search=python&_job_study_level=bac5-ou-plus&_job_exp_level=0-a-2-ans"
    
    def get_offers(self) -> list[Offer]:
        driver = self.driver
        
        driver.get(self.url)
        # driver.implicitly_wait(5)
        html_content = driver.page_source
        driver.quit()
        
        soup = BeautifulSoup(html_content, 'html.parser')

        # Trouver toutes les offers d'emploi
        offers = soup.find_all('li', class_='jobs-list__results-list-item')

        job_offers = []

        for offer in offers:
            title_element = offer.find('a')
            title = title_element.text.strip()
            link = title_element['href']
            contract = offer.find('p', class_='jobs-list__results-list-item-contract').text.strip()
            location = offer.find('p', class_='jobs-list__results-list-item-localisation').text.strip()
            domain = offer.find('p', class_='jobs-list__results-list-item-domain').text.strip()

            job_offers.append(
                Offer(
                    site = Site.get_by_id(1),
                    title = title,
                    description = None,
                    url = link,
                    date_publication = None,
                    location = location,
                    job_id = None
                )
            )
            
        return job_offers
        
if __name__ == "__main__":
    print(MBDAParser().compare_offers())
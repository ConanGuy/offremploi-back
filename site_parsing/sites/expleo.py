from site_parsing.data.orm import Offer, OfferGroup,Site

from ._parser import SiteParser

import time

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExpleoParser(SiteParser):
    
    site: Site = Site.get_by_id(3)
    url: str = site.url
    
    def get_offers(self, filters: dict = {}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        states = filter.get("state", ())
            
        job_offers = []
        for keyword in keywords:
            url = self.url.replace("[keyword]", keyword)
            
            driver = self.driver
            
            driver.get(url)
            wait = WebDriverWait(driver, 20)
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "icims_content_iframe")))
            
            html_content = driver.find_element(by=By.TAG_NAME, value="body").get_attribute('innerHTML')
            driver.quit()
            
            soup = BeautifulSoup(html_content, 'html.parser')

            # Trouver toutes les offers d'emploi
            offers = soup.find('div', class_='iCIMS_JobsTable').find_all('div', class_='row')
            
            for offer in offers:
                title_element = offer.find('a')
                job_id = title_element['title'].split(' - ')[0]
                title = " - ".join(title_element['title'].split(' - ')[1:])
                link = title_element['href']
                
                details_element = offer.find('dl', class_='iCIMS_JobHeaderGroup')
                details = details_element.find_all('dd')
                category = details[0].text.strip()
                contract = details[1].text.strip()
                location = details[2].text.strip()
                
                offer = Offer(
                    site = self.site,
                    title = title,
                    description = None,
                    url = link,
                    date_publication = None,
                    location = location,
                    job_id = job_id,
                    offer_group = offer_group, 
                )

                if not offer.exists() and any([state in offer.location for state in states]):
                    job_offers.append(offer)
                    
        return job_offers
        
if __name__ == "__main__":
    print(ExpleoParser().compare_offers())
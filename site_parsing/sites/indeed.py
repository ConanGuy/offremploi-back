from site_parsing.data.orm import Offer, OfferGroup, Site
from ._parser import SiteParser
from bs4 import BeautifulSoup, ResultSet
from datetime import date
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IndeedParser(SiteParser):
    
    site: Site = Site.get_by_id(9)
    url: str = site.url
    
    def get_offers(self, filters: dict = {}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        states = filter.get("state", ())
        
        # Get all possible combinantions of filters with keywords and states
        filters_combinations = []
        for state in states:
            for keyword in keywords:
                filters_combinations.append({"keyword": keyword, "state": state})
        
        job_offers: list[Offer] = []
        for combination in filters_combinations:
            keyword = combination["keyword"]
            state = combination["state"]
            url = self.url.replace("[keyword]", keyword).replace("[state]", state)

            driver = self.driver
            driver.get(url)
            try:
                # Handle cookies consent pop-up if present
                accept_cookies = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accepter')]"))
                )
                accept_cookies.click()
            except:
                pass  # If no cookie button is found, continue
            html_content = driver.page_source
            driver.quit()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            offers: list[ResultSet] = soup.find_all('div', class_='job_seen_beacon')

            for offer in offers:
                title = offer.find('h2', class_='jobTitle').text
                job_id = offer.find('a', class_='jcs-JobTitle')['id'].split("_")[-1]
                link = f"https://fr.indeed.com/viewjob?jk={job_id}"
                
                company_element = offer.find('div', class_='company_location')
                company = company_element.find("span", attrs={"data-testid": "company-name"}).text
                location = company_element.find("div", attrs={"data-testid": "text-location"}).text
                date_publication = date.today()

                offer = Offer(
                    site=self.site,
                    title=title,
                    description=company,
                    url=link,
                    date_publication=date_publication,
                    location=location,
                    job_id=job_id,
                    offer_group=offer_group
                )
                
                if not offer.exists():
                    job_offers.append(offer)
                
        return job_offers

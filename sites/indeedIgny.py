from data.orm import Offer
from data.orm import Site
from ._parser import SiteParser
from bs4 import BeautifulSoup, ResultSet
from datetime import date
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IndeedIgnyParser(SiteParser):
    
    site: Site = Site.get_by_id(9)
    url: str = site.url
    
    def get_offers(self) -> list[Offer]:
        driver = self.driver
        
        driver.get(self.url)
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

        job_offers: list[Offer] = []
        for offer in offers:
            title = offer.find('h2', class_='jobTitle').text
            job_id = offer.find('a', class_='jcs-JobTitle')['id'].replace("job_", "")
            link = f"https://fr.indeed.com/viewjob?jk={job_id}"
            job_id = offer.find('a', class_='jcs-JobTitle')['id']
            
            company_element = offer.find('div', class_='company_location')
            company = company_element.find("span", attrs={"data-testid": "company-name"}).text
            location = company_element.find("div", attrs={"data-testid": "text-location"}).text
            date_publication = date.today()

            job_offers.append(
                Offer(
                    site=self.site,
                    title=title,
                    description=company,
                    url=link,
                    date_publication=date_publication,
                    location=location,
                    job_id=job_id
                )
            )
        return job_offers

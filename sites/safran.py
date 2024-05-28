from data.orm import Offer
from data.orm import Site

from ._parser import SiteParser

from bs4 import BeautifulSoup, ResultSet
from datetime import datetime

class SafranParser(SiteParser):
    
    url: str = "https://www.safran-group.com/fr/offers?countries%5B0%5D=1002-france&regions_states%5B0%5D=33-ile-france&search=Python&contracts%5B0%5D=9-cdi&job_status%5B0%5D=3940-ingenieur-cadre&experiences%5B0%5D=3502-jeune-diplome-epremiere-experience&experiences%5B1%5D=6-superieure-3-ans&sort=date&items_per_page=All"
    
    def get_offers(self) -> list[Offer]:
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

            job_offers.append(
                Offer(
                    site = Site.get_by_id(0),
                    title = title,
                    description = None,
                    url = link,
                    date_publication = datetime.strptime(date, "%d.%m.%Y").date(),
                    location = location,
                    job_id = link.split("-")[-1],
                )
            )
        return job_offers
        

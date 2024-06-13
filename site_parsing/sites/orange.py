from site_parsing.data.orm import Offer, OfferGroup, Site
from ._parser import SiteParser
import requests
from datetime import datetime


class OrangeParser(SiteParser):

    site: Site = Site.get_by_id(5)  # Supposons que l'ID pour Orange est 5
    url: str = site.url
    
    def get_offers(self, filters: dict = {}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        states = filter.get("state", ())
        coordinates = ()
        for coord in filter.get("coordinates", ()):
            c1, c2 = coord.split("|")
            lat1, lon1 = c1.split(",")
            lat2, lon2 = c2.split(",")
            
            latmin = min(lat1, lat2)
            latmax = max(lat1, lat2)
            lngmin = min(lon1, lon2)
            lngmax = max(lon1, lon2)
            
            coordinates += ((latmin, latmax, lngmin, lngmax),)
        
        for coordinate in coordinates:
            latmin, latmax, lngmin, lngmax = coordinate
            
            payload = {
                "index": "1",
                "nb": 10000,
                "latmin": latmin,
                "latmax": latmax,
                "lngmin": lngmin,
                "lngmax": lngmax,
                "carto": "",
                "prelisteddomain": [],
                "contract": ["732"],
                "domain": keywords,
                "place": [],
            }
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
            }

            response = requests.post(self.url, json=payload, headers=headers)
            data: dict|list = response.json()

            job_offers = []
            for job in data.get("items", []):
                offer = Offer(
                    site=self.site,
                    title=job["title"],
                    description=None,
                    url="https://orange.jobs/jobs/v3/offers/" + str(job["id"]),
                    date_publication=datetime.strptime(
                        job["pubdate"], "%Y-%m-%d %H:%M:%S"
                    ).date(),
                    location=job["fulllocation"],
                    job_id=str(job["id"]),
                    offer_group=offer_group
                )
                
                if not offer.exists():
                    job_offers.append(offer)
                    
        return job_offers


if __name__ == "__main__":
    print(OrangeParser().compare_offers())

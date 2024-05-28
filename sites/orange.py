from data.orm import Offer
from data.orm import Site
from ._parser import SiteParser
import requests
from datetime import datetime


class OrangeParser(SiteParser):

    site: Site = Site.get_by_id(5)  # Supposons que l'ID pour Orange est 5
    url: str = site.url

    def get_offers(self) -> list[Offer]:
        payload = {
            "index": "1",
            "nb": 10000,
            "latmin": "48.402767712529176",
            "latmax": "48.79193783965157",
            "lngmin": "1.9473266601562502",
            "lngmax": "2.2906494140625004",
            "carto": "",
            "prelisteddomain": [],
            "contract": ["732"],
            "domain": ["python"],
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
            )
            
            job_offers.append(offer)
        return job_offers


if __name__ == "__main__":
    print(OrangeParser().compare_offers())

from site_parsing.data.orm import Offer, OfferGroup, Site
from ._parser import SiteParser

from datetime import datetime

import json
import os
import requests

class DanoneParser(SiteParser):

    site: Site = Site.get_by_id(7)
    url: str = site.url

    def get_offers(self, filters: dict={}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        country = "+".join(filter.get("country", ()))
        states = filter.get("state", ())
        
        url = "https://careers.danone.com/bin/jobs.json?search=[keyword]&countries={country}&experience=Experienced%20Professionals%2BGraduates&locale=fr-FR&limit=30"
        url = url.replace("{country}", country)
        
        headers = {
            "accept": "*/*",
            "accept-language": "fr-FR",
            "cookie": "TCPID=124531915362546099644; TC_PRIVACY=0%40005%7C93%7C5327%402%2C4%401%401715188539662%2C1715188539662%2C1748884539662%40; TC_PRIVACY_CENTER=2%2C4; _gcl_au=1.1.911053065.1715188540; affinity=\"8bd5e67cdee0b81b\"; _gid=GA1.2.2117142566.1715884504; _ga=GA1.1.2101152343.1715188540; _ga_K3MW8J5Y6B=GS1.1.1715884504.3.1.1715884532.32.0.0",
            "priority": "u=1, i",
            "referer": "https://careers.danone.com/",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        
        job_offers = []
        for keyword in keywords:
            self.url = url.replace("[keyword]", keyword)
            
            response = requests.get(self.url, headers=headers)
            with open("danone.json", "w", encoding="utf-8") as f:
                f.write(response.text)
            data = json.load(open("danone.json", "r"))
            os.remove("danone.json")

            for job in data.get("results", []):
                offer = Offer(
                    site=self.site,
                    title=job["title"],
                    description=None, 
                    url="https://careers.danone.com/fr/fr/opportunites/" + job["url"],
                    date_publication=datetime.fromtimestamp(int(job["posted"]) / 1000).date(),
                    location=job["city"],
                    job_id=job["jobId"],
                    offer_group=offer_group
                )
    
                if not offer.exists() and self.departement_from_ville(offer.location) in states:
                    job_offers.append(offer)
                
        return job_offers

if __name__ == "__main__":
    print(DanoneParser().compare_offers())

from site_parsing.data.orm import Offer, OfferGroup, Site

from ._parser import SiteParser

import requests
from datetime import datetime


class ThalesParser(SiteParser):

    site: Site = Site.get_by_id(4)
    url: str = site.url
    
    def get_offers(self, filters: dict = {}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        states = filter.get("state", ())
        
        job_offers = []
        for keyword in keywords:
            payload = {
                "lang": "fr_fr",
                "deviceType": "desktop",
                "country": "fr",
                "pageName": "search-results",
                "ddoKey": "refineSearch",
                "sortBy": "Most recent",
                "subsearch": keyword,
                "from": 0,
                "jobs": True,
                "counts": True,
                "all_fields": [
                    "category",
                    "country",
                    "state",
                    "city",
                    "type",
                    "workerSubType",
                    "workLocation",
                ],
                "size": 100,
                "clearAll": False,
                "jdsource": "facets",
                "isSliderEnable": False,
                "pageId": "page18",
                "siteType": "external",
                "keywords": "",
                "global": True,
                "selected_fields": {
                    "state": states,
                    "workerSubType": ["Regular Employee"],
                    "type": ["Full time"],
                },
                "sort": {"order": "desc", "field": "postedDate"},
                "locationData": {},
            }
            headers = {
                "Content-Type": "application/json",
            }

            response = requests.post(self.url, json=payload, headers=headers)
            data = response.json()

            for job in data["refineSearch"]["data"]["jobs"]:
                offer = Offer(
                    site=self.site,
                    title=job["title"],
                    description=job["descriptionTeaser"],
                    url="https://careers.thalesgroup.com/fr/fr/job/" + job["jobId"],
                    date_publication=datetime.strptime(
                        job["postedDate"], "%Y-%m-%dT%H:%M:%S.%f%z"
                    ).date(),
                    location=job["cityStateCountry"],
                    job_id=job["jobId"],
                    offer_group=offer_group,
                )

                if not offer.exists():
                    job_offers.append(offer)
                    
        return job_offers


if __name__ == "__main__":
    print(ThalesParser().compare_offers())

from site_parsing.data.orm import Offer, OfferGroup, Site

from ._parser import SiteParser

import requests
from datetime import date


class AirbusParser(SiteParser):

    site: Site = Site.get_by_id(13)
    url: str = site.url

    def get_offers(self, filters: dict = {}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]

        keywords = filter.get("keyword", ())
        states = filter.get("state", ())

        states_ids = {
            "Essonne": "f5811cef9cb50156ca250d694c0a8c44",
            "Yvelines": "f5811cef9cb50156ca250d694c0a8c44",
            "Gironde": "f5811cef9cb5014f0556f06a4c0ae04a",
            "Haute-Garonne": "f5811cef9cb501ede9109d684c0afc42",
        }
        states_filtered = [states_ids[state] for state in states if state in states_ids]       
        
        if len(states_filtered) == 0:
            return []    

        job_offers = []
        for keyword in keywords:
            payload = {
                "appliedFacets": {
                    "hiringCompany": [
                        "f5811cef9cb50166ff1fba124e0a295c",
                        "f5811cef9cb501eb3bf4e0124e0add5c",
                        "f5811cef9cb5013b35f9bb124e0a335c",
                    ],
                    "locationCountry": ["54c5b6971ffb4bf0b116fe7651ec789a"],
                    "locations": states_filtered,
                },
                "workerSubType": ["f5811cef9cb501a69768a71d470a6d15"],
                "limit": 20,
                "offset": 0,
                "searchText": keyword,
            }

            response = requests.post(self.url, json=payload)
            data = response.json()

            for job in data["jobPostings"]:
                offer = Offer(
                    site=self.site,
                    title=job["title"],
                    description=None,
                    url="https://ag.wd3.myworkdayjobs.com/fr-FR/Airbus" + job["externalPath"],
                    date_publication=date.today(),
                    location=job["locationsText"],
                    job_id=job["bulletFields"][0],
                    offer_group=offer_group,
                )

                if not offer.exists():
                    job_offers.append(offer)

        return job_offers


if __name__ == "__main__":
    print(AirbusParser().compare_offers())

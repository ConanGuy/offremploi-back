from site_parsing.data.orm import Offer, OfferGroup, Site

from ._parser import SiteParser

import requests
from datetime import datetime


class DassaultParser(SiteParser):

    site: Site = Site.get_by_id(2)
    url: str = site.url

    def get_offers(self, filters: dict={}) -> list[Offer]:
        offer_group_id = list(filters.keys())[0]                
        offer_group = OfferGroup.get_by_id(offer_group_id)
        filter: dict = filters[offer_group_id]
        
        keywords = filter.get("keyword", ())
        country = '(' + " OR ".join(f"(%22pays%2F{s}%22)" for s in filter.get("country", ())) + ')'        
        state = '(' + " OR ".join([f"(%22ville%2FFrance, {self.departement_from_nom(s)['code']}%22)" for s in filter.get("state", ())]) + ')'

        experience = '(' + " OR ".join(f"(%22year%2F{s.replace(' ', '%20')}%22)" for s in filter.get("experience", ("0 to 3 years", "4 to 5 years"))) + ')'

        contract_type = "(%22type%20de%20contrat%2Fcdi%22)"
        
        q = " AND ".join([country, state, experience, contract_type])
        url = self.url.replace("{q}", q)
        
        headers = {
            "Content-Type": "application/json",
        }

        job_offers = []
        for keyword in keywords:
            current_url = url.replace("[keyword]", keyword)
            
            response = requests.post(current_url, headers=headers)
            data = response.json()

            for hit in data["hits"]:
                offer = Offer(
                    site=self.site,
                    title=next(
                        (
                            meta["value"]
                            for meta in hit["metas"]
                            if meta["name"] == "content_title"
                        ),
                        None,
                    ),
                    description=None,
                    url=next(
                        (
                            meta["value"]
                            for meta in hit["metas"]
                            if meta["name"] == "content_cta_1_url"
                        ),
                        None,
                    ),
                    date_publication=datetime.strptime(
                        next(
                            (
                                meta["value"]
                                for meta in hit["metas"]
                                if meta["name"] == "content_start_datetime"
                            ),
                            None,
                        ),
                        "%Y/%m/%d %H:%M:%S",
                    ).date(),
                    location=next(
                        (
                            meta["value"]
                            for meta in hit["metas"]
                            if meta["name"] == "content_info_2_value"
                        ),
                        None,
                    ),
                    job_id=next(
                        (
                            meta["value"]
                            for meta in hit["metas"]
                            if meta["name"] == "card_id"
                        ),
                        None,
                    ),
                    offer_group=offer_group
                )

                if not offer.exists():
                    job_offers.append(offer)
        return job_offers


if __name__ == "__main__":
    print(DassaultParser().compare_offers())

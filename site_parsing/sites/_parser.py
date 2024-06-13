from site_parsing.data.orm import Offer, OfferGroup, Site

from seleniumbase import Driver
from selenium.webdriver import Chrome

import requests, json

class SiteParser:
    
    site: Site
    url: str
    @property
    def driver(self) -> Chrome: return Driver(uc=True, headless2=True, browser="chrome")
    
    def get_offers_(self, offer_groups: dict={}) -> list[Offer]:
        offers = []
        for offer_group_id, filters in offer_groups.items():
            new_offers = self.get_offers({offer_group_id: filters})
            offers += new_offers
            print(f"Found {len(new_offers)} offers for {self.__class__.__name__} (filter: {OfferGroup.get_by_id(offer_group_id).name})")                
        return offers
    
    def get_offers(self, *args, **kwargs): ...
    
    def add_offers(self, offers: list[Offer] = None):
        if offers is None:
            offers = self.get_offers()
            
        for offer in offers:
            if not offer.exists():
                offer.add()        
                
    ### GEO API ###
                
    def commune_from_code_postal(self, code:str):
        try:
            url = f"https://geo.api.gouv.fr/communes?codePostal={code}"
            response = requests.get(url)
            data = json.loads(response.text)
            return data[0]
        except:
            return None
    
    def commune_from_nom(self, ville:str):
        try:
            url = f"https://geo.api.gouv.fr/communes?nom={ville.lower()}&format=json"
            response = requests.get(url)
            data = json.loads(response.text)
            return data[0]
        except:
            return None
    
    def departement_from_code(self, code:str):
        try:
            url = f"https://geo.api.gouv.fr/departements?code={code}&format=json"
            response = requests.get(url)
            data = json.loads(response.text)
            return data[0]
        except:
            return None
    
    def departement_from_nom(self, nom:str):
        try:
            url = f"https://geo.api.gouv.fr/departements?nom={nom.lower()}&format=json"
            response = requests.get(url)
            data = json.loads(response.text)
            return data[0]
        except:
            return None
    
    def departement_from_ville(self, ville:str):
        try:
            code = self.commune_from_nom(ville)["codeDepartement"]
            return self.departement_from_code(code)
        except:
            return None
            
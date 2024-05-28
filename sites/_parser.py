from data.orm import Offer

from seleniumbase import Driver
from selenium.webdriver import Chrome

class SiteParser:
    
    url: str
    @property
    def driver(self) -> Chrome: return Driver(uc=True, headless2=True, browser="chrome")
    
    def get_offers(self): ...

    def compare_offers(self) -> list[Offer]:
        offers = self.get_offers()
        
        sites_possibles: set[str] = {offer.site.id for offer in offers}
        offers_existantes: list[Offer] = [offer for offer in Offer.get_all() if offer.site.id in sites_possibles]
        
        attributs: list[str] = [attr for attr in Offer.get_attributes() if attr != "id"]
        
        nouvelles_offers: list[Offer] = []
        offer: Offer
        for offer in offers:
            est_nouvelle: bool = True
            for offer_existante in offers_existantes:
                if offer.site.id == offer_existante.site.id and offer.job_id != None and offer.job_id == offer_existante.job_id:
                    est_nouvelle = False
                    break
                
                if all([offer.__getattribute__(attr) == offer_existante.__getattribute__(attr) for attr in attributs]):
                    est_nouvelle = False
                    break
            
            if est_nouvelle:
                nouvelles_offers.append(offer)
                
        return nouvelles_offers
    
    def add_offers(self, offers: list[Offer] = None):
        if offers is None:
            offers = self.compare_offers()
            
        for offer in offers:
            offer.add()
            
            
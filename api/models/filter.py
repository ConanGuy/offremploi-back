from django.db import models

from .offer_group import OfferGroup

class Filter(models.Model):
    offer_group = models.ForeignKey(OfferGroup, on_delete=models.CASCADE, related_name='filters', null=False)
    
    # Possible keys:
    # - keyword: python, java, ...
    # - country: France, Allemagne, Espagne, ...
    # - state: Essonne, Yvelines, ...
    # - city: Paris, Ile-de-France, ...
    # - experience: Junior, Senior, Confirmé, Débutant
    # - contract_type: CDI, CDD, Stage, Alternance, Intérim, Freelance
    # - job_status: Temps plein, Temps partiel
    # - study_level: Bac, Bac+2, Bac+3, Bac+4, Bac+5, Bac+8
    # - latitude_min
    # - latitude_max
    # - longitude_min
    # - longitude_max
    # - radius
    
    key = models.CharField(max_length=255, null=False)
    value = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return f"{self.offer_group.name} - {self.key} - {self.value}"

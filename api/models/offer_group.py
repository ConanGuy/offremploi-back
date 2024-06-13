from django.db import models

from .site import Site

class OfferGroup(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    
    def __str__(self):
        return f"{self.name}"

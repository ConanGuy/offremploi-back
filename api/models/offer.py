from django.db import models

from .site import Site
from .offer_group import OfferGroup

class Offer(models.Model):
    offer_group = models.ForeignKey(OfferGroup, on_delete=models.CASCADE, related_name='offers', null=False)
    date_insertion = models.DateField(auto_now_add=True, null=False)
    lu = models.BooleanField(auto_created=True, default=False, null=False)
    title = models.CharField(max_length=255, null=False)
    url = models.CharField(max_length=255, null=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='offres', null=False)
    location = models.CharField(max_length=255, blank=True, null=True)
    date_publication = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    job_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.site.name} - {self.title} - {self.date_publication}"

from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=255, null=False)
    url = models.CharField(max_length=255, null=False)
    is_filtered = models.BooleanField(null=False)

    def __str__(self):
        return self.name

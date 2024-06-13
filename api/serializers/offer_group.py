from api.serializers.site import SiteSerializer

from ..models import OfferGroup

from rest_framework import serializers

class OfferGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferGroup
        fields = '__all__'
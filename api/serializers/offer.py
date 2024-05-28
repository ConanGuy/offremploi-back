from api.serializers.site import SiteSerializer

from ..models import Offer

from rest_framework import serializers

class OfferSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)
    
    class Meta:
        model = Offer
        fields = '__all__'

class OfferReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['lu']
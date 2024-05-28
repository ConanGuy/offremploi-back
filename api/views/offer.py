from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Offer
from api.serializers.offer import OfferSerializer
from ..serializers import OfferSerializer, OfferReadSerializer
from django_filters import rest_framework as filters

class OfferFilter(filters.FilterSet):
    lu = filters.BooleanFilter(field_name='lu')
    order = filters.OrderingFilter(
        fields=(
            ('date_insertion', 'date'),
            ('site__id', 'site'),
        ),
        field_labels={
            'date': 'Date de publication',
            'site': 'Site',
        }
    )

    class Meta:
        model = Offer
        fields = ['lu', 'order']
    
class OfferListCreate(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfferFilter

class OfferRetrieve(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    
class OfferRead(generics.UpdateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferReadSerializer

    def update(self, request, *args, **kwargs):
        # Si le corps de la requête est vide, mettez à jour 'lu' à true par défaut
        if not request.data:
            request.data['lu'] = True

        return super().update(request, *args, **kwargs)

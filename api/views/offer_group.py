from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, response

from .offer import OfferFilter, OfferListCreate
from ..models import OfferGroup
from ..serializers import OfferGroupSerializer

class OfferGroupList(generics.ListAPIView):
    queryset = OfferGroup.objects.all()
    serializer_class = OfferGroupSerializer
    
    # Modify the queryset to remove when id<0
    def get_queryset(self):
        return OfferGroup.objects.filter(id__gte=0)
    
class OfferGroupRetrieve(generics.RetrieveAPIView):
    queryset = OfferGroup.objects.all()
    serializer_class = OfferGroupSerializer
        
class OfferGroupRetrieveWithOffers(generics.RetrieveAPIView):
    queryset = OfferGroup.objects.all()
    serializer_class = OfferGroupSerializer

    def get(self, request, *args, **kwargs):        
        offer_group = self.get_object()
        offer_group_data = OfferGroupSerializer(offer_group).data
        
        offers = OfferListCreate.as_view()(request._request).data
        offers = [offer for offer in offers if offer['offer_group']['id'] == offer_group.id]
        
        offer_group_data['offers'] = offers
        
        return response.Response(offer_group_data)
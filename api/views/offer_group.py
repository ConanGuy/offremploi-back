from rest_framework import generics, response, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .offer import OfferFilter, OfferListCreate
from ..models import OfferGroup, Offer
from ..serializers import OfferGroupSerializer, OfferSerializer

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
    queryset = OfferGroup.objects.all().prefetch_related('offers')
    serializer_class = OfferGroupSerializer

    def get_filtered_offers(self, offer_group, request):
        # Retrieve filters from the request query params
        filters = OfferFilter(data=request.query_params, queryset=Offer.objects.filter(offer_group=offer_group))
        return filters.qs

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('lu', openapi.IN_QUERY, description="Filter by lu", type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('order', openapi.IN_QUERY, description="Order by date or site", type=openapi.TYPE_STRING, enum=['date', '-date', 'site', '-site']),
    ])
    def get(self, request, *args, **kwargs):
        offer_group = self.get_object()
        offer_group_data = OfferGroupSerializer(offer_group).data
        
        offers = self.get_filtered_offers(offer_group, request)
        
        offer_group_data['offers'] = OfferSerializer(offers, many=True).data

        return response.Response(offer_group_data, status=status.HTTP_200_OK)
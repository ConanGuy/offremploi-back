from rest_framework import generics
from ..models import Site
from ..serializers import SiteSerializer

class SiteListCreate(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteRetrieve(generics.RetrieveAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    
    

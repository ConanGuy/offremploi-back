from rest_framework import generics
from ..models import Site
from ..serializers import SiteSerializer

class SiteCreate(generics.CreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteRetrieve(generics.RetrieveAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

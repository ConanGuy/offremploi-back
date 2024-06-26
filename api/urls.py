"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import SiteListCreate, SiteRetrieve, OfferListCreate, OfferRetrieve, OfferRead, OfferGroupList, OfferGroupRetrieveWithOffers, OfferGroupRetrieve
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Offremploi API Documentation",
      default_version='v1',
      description="API documentation for Offremploi",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/sites/', SiteListCreate.as_view(), name='site_list_create'),
    path('api/sites/<int:pk>/', SiteRetrieve.as_view(), name='site_detail'),
    path('api/offers/', OfferListCreate.as_view(), name='offre_list_create'),
    path('api/offers/<int:pk>/', OfferRetrieve.as_view(), name='offre_detail'),
    path('api/offers/<int:pk>/read/', OfferRead.as_view(), name='offer_read'),
    path('api/offergroups/', OfferGroupList.as_view(), name='offer_groups'),
    path('api/offergroups/<int:pk>/', OfferGroupRetrieve.as_view(), name='offer_groups_detail'),
    path('api/offergroups/<int:pk>/offers/', OfferGroupRetrieveWithOffers.as_view(), name='offer_groups_with_offers'),
]
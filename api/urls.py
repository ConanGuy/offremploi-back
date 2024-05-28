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
from .views import SiteCreate, SiteRetrieve, OfferListCreate, OfferRetrieve, OfferRead

urlpatterns = [
    path('api/sites/', SiteCreate.as_view(), name='site_list_create'),
    path('api/sites/<int:pk>/', SiteRetrieve.as_view(), name='site_detail'),
    path('api/offers/', OfferListCreate.as_view(), name='offre_list_create'),
    path('api/offers/<int:pk>/', OfferRetrieve.as_view(), name='offre_detail'),
    path('api/offers/<int:pk>/read/', OfferRead.as_view(), name='offer_read'),
]
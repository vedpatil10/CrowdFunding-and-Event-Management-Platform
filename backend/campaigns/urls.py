from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'campaigns', views.CampaignViewSet)
router.register(r'donations', views.CampaignDonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

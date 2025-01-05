from django.urls import path,include
from .views import SettlementViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list',SettlementViewset)

urlpatterns = [
    path('', include(router.urls)),
]

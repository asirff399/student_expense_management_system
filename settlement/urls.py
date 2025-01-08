from django.urls import path,include
from .views import SettlementViewset,PaymentAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list',SettlementViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('payment/<int:settlement_id>/', PaymentAPIView.as_view(),name='payment'),
]

from django.urls import path,include
from .views import CategoryViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list',CategoryViewset)

urlpatterns = [
    path('', include(router.urls)),
]

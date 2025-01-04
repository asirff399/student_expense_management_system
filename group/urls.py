from django.urls import path,include
from .views import GroupViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list',GroupViewset)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path,include
from .views import ExpensesViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list',ExpensesViewset)

urlpatterns = [
    path('', include(router.urls)),
]

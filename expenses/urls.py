from django.urls import path,include
from .views import ExpensesViewset,ExpenseCreateView,MonthlyAnalysisView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list',ExpensesViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('post/', ExpenseCreateView.as_view(),name='expense_create'), 
    path('monthly_analysis/', MonthlyAnalysisView.as_view(),name='monthly_analysis'), 
]

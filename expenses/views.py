from django.shortcuts import render
from rest_framework import viewsets
from .models import Expenses
from .serializers import ExpensesSerializers

# Create your views here.
class ExpensesViewset(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializers
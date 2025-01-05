from django.shortcuts import render
from rest_framework import viewsets
from .models import Settlement
from .serializers import SettlementSerializers

# Create your views here.
class SettlementViewset(viewsets.ModelViewSet):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializers

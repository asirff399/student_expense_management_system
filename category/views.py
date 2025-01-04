from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializers

# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

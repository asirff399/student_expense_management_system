from django.shortcuts import render
from rest_framework import viewsets
from .models import Group
from .serializers import GroupSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        student = user.student
        return Group.objects.filter(members=student)
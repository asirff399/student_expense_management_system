from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Settlement
from .serializers import SettlementSerializer
from django.db import models

# Create your views here.
class SettlementViewset(viewsets.ModelViewSet):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        student = user.student
        return Settlement.objects.filter(models.Q(payer=student) | models.Q(payee=student))
    
    def perform_create(self, serializer):
        serializer.save()

class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, settlement_id):
        try:
            settlement = Settlement.objects.get(id=settlement_id, payer=request.user.student)
            if settlement.payment_status == 'completed':
                return Response({'message':'Payment already completed.'}, status=status.HTTP_400_BAD_REQUEST)
            
            settlement.payment_status = 'completed'
            settlement.save()

            return Response({'message':'Payment successfull.'},status=status.HTTP_200_OK)
        
        except Settlement.DoesNotExist:
            return Response({'error':'Settlement not found or unauthorized access.'},status=status.HTTP_400_BAD_REQUEST)
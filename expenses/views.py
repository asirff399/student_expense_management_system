from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Expenses
from .serializers import ExpensesSerializers
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth

# Create your views here.
class ExpensesViewset(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializers

class ExpenseCreateView(APIView):
    serializer_class = ExpensesSerializers
    
    def post(self, request):
        serializer = ExpensesSerializers(data=request.data)
        if serializer.is_valid():
            expense = serializer.save()
            return Response({'message':'Expense recorded successfully', 'expense_id': expense.id}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MonthlyAnalysisView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        student = user.student

        monthly_expenses = (
            Expenses.objects.filter(group__members = student)
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(total_spent=Sum('amount'))
        )

        category_summary = (
            Expenses.objects.filter(group__members=student)
            .values('category__name')
            .annotate(total_spent=Sum('amount'))
        )

        group_summary = (
            Expenses.objects.filter(group__members=student)
            .values('group__name')
            .annotate(total_spent=Sum('amount'))
        )

        data = {
            "monthly_expenses": monthly_expenses,
            "category_summary": {item['category__name']: item['total_spent'] for item in category_summary},
            "group_summary": {item['group__name']: item['total_spent'] for item in group_summary},
        }
        return Response(data)
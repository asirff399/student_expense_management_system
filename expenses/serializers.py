from rest_framework import serializers
from .models import Expenses

class ExpensesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'
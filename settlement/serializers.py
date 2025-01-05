from rest_framework import serializers
from .models import Settlement

class SettlementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = '__all__'
from rest_framework import serializers
from .models import Settlement

class SettlementSerializer(serializers.ModelSerializer):
    payer_name = serializers.ReadOnlyField(source='payer.user.get_full_name')
    payee_name = serializers.ReadOnlyField(source='payee.user.get_full_name')

    class Meta:
        model = Settlement
        fields =['id','payment_status','settlement_method','due_date','amount','payer','payer_name','payee','payee_name']
    
    def validate(self, data):
        if data['payer'] == data['payee']:
            raise serializers.ValidationError("Payer and payee cannot be the same.")
        return data
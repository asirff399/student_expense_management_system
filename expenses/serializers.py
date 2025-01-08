from rest_framework import serializers
from .models import Expenses

class ExpensesSerializers(serializers.ModelSerializer):
    shares = serializers.DictField(write_only=True, required=False)

    class Meta:
        model = Expenses
        fields = '__all__'

    def validate(self, data):
        group = data.get('group')
        if not group:
            raise serializers.ValidationError('Group is required.')
        
        if data['paid_by'] not in group.members.all():
            raise serializers.ValidationError("The payer must be a member of the group.")
        
        if data['split_type'] == 'custom':
            shares = data.get('shares',{})
            if not shares or sum(shares.values()) != data['amount']:
                raise serializers.ValidationError('Custom shares must sum up to the total amount.')
            if not all(student_id in group.members.values_list('id',flat=True) for student_id in shares.keys()):
                raise serializers.ValidationError("All custom share members must be part of the group.")
        
        return data
    
    def create(self, validated_data):
        split_type = validated_data.pop('split_type')
        shares = validated_data.pop('shares',{})
        group = validated_data['group']
        amount = validated_data['amount']
        paid_by = validated_data['paid_by']

        expense = Expenses.objects.create(**validated_data, split_type=split_type)

        if split_type == 'equal':
            share_amount = amount / group.members.count()
            for member in group.members.all():
                print(f"Assigning {share_amount} to {member}")
        elif split_type == 'custom':
            for student_id, share_amount in shares.items():
                student = group.members.get(id=student_id)
                print(f'Assigning {share_amount} to {student}')
        return expense
    
class MonthlyAnalysisSerializer(serializers.Serializer):
    month = serializers.DateField()
    total_spent = serializers.DecimalField(max_digits=10, decimal_places=2)
    category_summary = serializers.DictField(child=serializers.DecimalField(max_digits=10,decimal_places=2)) 
    group_summary = serializers.DictField(child=serializers.DecimalField(max_digits=10,decimal_places=2))


from rest_framework import serializers
from .models import Group
from account.models import Student

# class GroupSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), many=True)

    class Meta:
        model = Group
        fields = ['id','name','group_type','members']
    
    def validate_members(self, members):
        if len(members) < 2:
            raise serializers.ValidationError("A group must have at least 2 members.")
        return members
    
    def create(self, validateed_data):
        members = validateed_data.pop('members')
        group = Group.objects.create(**validateed_data)
        group.members.set(members)
        return group

    def update(self,instance,validated_data):
        members = validated_data.pop('members',None)
        if members is not None:
            instance.members.set(members)
        for attr,value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        return instance
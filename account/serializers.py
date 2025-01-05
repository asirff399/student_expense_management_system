from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student



class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']

    def save(self,**kwargs):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error':"Password don't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email already exists"})
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error':"Username already exists"})
        
        user = User(username=username,email=email,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.is_active = False
        user.save()

        student = Student(user=user)
        student.save()

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
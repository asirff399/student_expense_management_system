from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializers import RegistrationSerializer,LoginSerializer,StudentSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken,TokenError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.
class UserRegisterAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            access = AccessToken.for_user(user=user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f'http://127.0.0.1:8000/account/active/{uid}/{access}'
            email_subject = "Confirmation Email"
            email_body = render_to_string('confirmation_email.html',{'confirm_link':confirm_link})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response({'error':'Check your mail for confirmation.'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
        return redirect('http://127.0.0.1:8000/account/register/') 
    
    try:
        access = AccessToken(token)
        if user is not None and not user.is_active:
            user.is_active =True
            user.save()
            return redirect('http://127.0.0.1:8000/account/login/')
        else:
            return redirect('http://127.0.0.1:8000/account/login/')
    except Exception:
        return redirect('http://127.0.0.1:8000/account/register/') 

class UserLoginAPIView(APIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = LoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                login(request,user)

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user_id': user.id,
                    'message':"Logged in Successfully!",
                },status=status.HTTP_200_OK)
            else:
                return Response({'error':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'user':['exact']} 

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer






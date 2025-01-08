from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegisterAPIView,activate,UserLoginAPIView,StudentViewset,UserViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('student/list',StudentViewset)
router.register('users/list',UserViewset) 

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('active/<uid64>/<token>/', activate, name='activate'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
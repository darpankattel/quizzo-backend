from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from core.response import MyResponse
from .serializers import AuthSerializer, UserProfileSerializer, ProfileWriteSerializer, UserAllSerializer
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated


class LoginView(KnoxLoginView):
    """
    Login View extending the Knox LoginView
    """
    serializer_class = AuthSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        if request.data.get("password") != request.data.get("confirm_password"):
            return MyResponse.failure(message="Passwords do not match")
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            profile_serializer = ProfileWriteSerializer(
                data={**request.data, "user": serializer.data["id"]})
            if profile_serializer.is_valid():
                profile_serializer.save()
                return MyResponse.success(data=UserAllSerializer(User.objects.get(id=serializer.data["id"])).data, message="User registered successfully")
        return MyResponse.failure(message=serializer.errors)


class ProfileView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        serializer = UserAllSerializer(request.user)
        return MyResponse.success(data=serializer.data, message="Profile fetched successfully")

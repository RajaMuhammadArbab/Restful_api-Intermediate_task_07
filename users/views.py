from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from .serializers import UserListSerializer, UserDetailSerializer

# --- User List (GET /api/users/) ---
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]

# --- User Detail (GET /api/users/{id}/) ---
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]

# --- Register New User (POST /api/users/register/) ---
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_staff", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

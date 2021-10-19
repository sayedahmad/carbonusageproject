from rest_framework import permissions
from django.contrib.auth import get_user_model  # If used custom user model
from django.contrib.auth.models import User  # Builtiin User Model
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializer import UserSerializer


class CreateUserView(ListCreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.IsAdminUser  # Or anon users can't register
    ]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateView(UpdateAPIView):
    model = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser  # Or anon users can't update
    ]


class UserDeleteView(DestroyAPIView):
    model = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser  # Or anon users can't delete
    ]

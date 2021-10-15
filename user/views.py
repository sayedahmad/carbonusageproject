from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, 
    ListCreateAPIView, 
    UpdateAPIView, 
    DestroyAPIView
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .serializer import UserSerializer
from .models import User

# Create your views here.


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class=PageNumberPagination
    permission_classes = (IsAuthenticated,)


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

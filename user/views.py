from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, 
    ListCreateAPIView, 
    UpdateAPIView, 
    DestroyAPIView
)
from rest_framework.pagination import PageNumberPagination

from .serializer import UserSerializer
from .models import User

# Create your views here.


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class=PageNumberPagination


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

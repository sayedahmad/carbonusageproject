from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    UpdateAPIView,
)
from rest_framework.pagination import PageNumberPagination
from .models import Usage, UsageType
from .serializer import UsageTypeSerializer, UsageSerializer
# Create your views here


class UsageTypeView(ListAPIView):
    queryset = UsageType.objects.all()
    serializer_class = UsageTypeSerializer
    pagination_class = PageNumberPagination


class UsageTypeCreateView(ListCreateAPIView):
    queryset = UsageType.objects.all()
    serializer_class = UsageSerializer


class UsageTypeUpdateView(UpdateAPIView):
    queryset = UsageType.objects.all()
    serializer_class = UsageSerializer


class UsageTypeDeleteView(DestroyAPIView):
    queryset = UsageType.objects.all()
    serializer_class = UsageSerializer


class UsageCreateView(ListCreateAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
    pagination_class = PageNumberPagination


class UsageUpdateView(UpdateAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer


class UsageDeleteView(DestroyAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer

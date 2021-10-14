from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    UpdateAPIView,
)
from .models import Usage, UsageType
from .serializer import UsageTypeSerializer, UsageSerializer
# Create your views here


class UsageTypeView(ListAPIView):
    queryset = UsageType.objects.all()
    serializer_class = UsageTypeSerializer

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


class UsageUpdateView(UpdateAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
class UsageDeleteView(DestroyAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer

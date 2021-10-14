from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Usage, Usage_type
from .serializer import UsageTypeSerializer, UsageSerializer
# Create your views here


class UsageTypeView(ListAPIView):
    queryset = Usage_type.objects.all()
    serializer_class = UsageTypeSerializer

class UsageView(ListAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
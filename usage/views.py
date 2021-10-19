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
from rest_framework.permissions import IsAuthenticated

from .models import Usage, UsageType
from .serializer import UsageTypeSerializer, UsageSerializer
# Create your views here


class UsageTypeView(ListAPIView):
    queryset = UsageType.objects.all()
    serializer_class = UsageTypeSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated,)


class UsageTypeCreateView(ListCreateAPIView):
    queryset = UsageType.objects.all()
    serializer_class = UsageSerializer
    permission_classes = (IsAuthenticated,)


class UsageTypeUpdateView(UpdateAPIView):
    queryset = UsageType.objects.all()
    serializer_class = UsageSerializer
    permission_classes = (IsAuthenticated,)


class UsageTypeDeleteView(DestroyAPIView):
    queryset = UsageType.objects.all()
    serializer_class = UsageSerializer
    permission_classes = (IsAuthenticated,)


class UsageView(ListAPIView):
    serializer_class = UsageSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ get parameters from get url """
        sort = self.request.query_params.get('sort') 
        startdate = self.request.query_params.get('startdate')
        enddate = self.request.query_params.get('enddate')
        queryset = Usage.objects.all()

        """ sor by asc desc"""
        if sort == "asc":
            queryset = Usage.objects.order_by('usage_at')
        if sort == "desc":
            queryset = Usage.objects.order_by('-usage_at')
        
        if startdate and enddate:
            """Filter by start and end date"""
            queryset = Usage.objects.filter(
                usage_at__gte=startdate, usage_at__lte=enddate)

        return queryset


class UsageCreateView(ListCreateAPIView):
    serializer_class = UsageSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated,)


class UsageUpdateView(UpdateAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
    permission_classes = (IsAuthenticated,)


class UsageDeleteView(DestroyAPIView):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
    permission_classes = (IsAuthenticated,)

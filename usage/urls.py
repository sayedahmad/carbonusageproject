from django.urls import path
from .views import (
    UsageTypeView,
    UsageTypeCreateView,
    UsageTypeUpdateView,
    UsageTypeDeleteView,

    UsageCreateView,
    UsageUpdateView,
    UsageDeleteView,
    UsageView,
)

urlpatterns = [
    path('type/', UsageTypeView.as_view(), name='usagetype'),
    path('type/add/', UsageTypeCreateView.as_view(), name='usagetype'),
    path('type/update/<int:pk>/', UsageTypeUpdateView.as_view(),
         name='usagetypeupdate'),
    path('type/delete/<int:pk>/', UsageTypeDeleteView.as_view(),
         name='usagetypedelete'),

    path('', UsageView.as_view(), name='usage'),
    path('add/', UsageCreateView.as_view(), name='usage'),
    path('update/<int:pk>/', UsageUpdateView.as_view(), name='usageupdate'),
    path('delete/<int:pk>/', UsageDeleteView.as_view(), name='usagedelete'),
]

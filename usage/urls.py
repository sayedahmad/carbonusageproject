from django.urls import path
from .views import UsageTypeView, UsageView
urlpatterns = [
    path('usagetype/', UsageTypeView.as_view(), name='usagetype'),
    path('usage/', UsageView.as_view(), name='usage'),
]

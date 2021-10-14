from django.urls import path
from .views import (
    UserView,
    UserUpdateView,
    UserDeleteView,
)

urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='userupdate'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='userupdate'),
]

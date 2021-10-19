from django.urls import path
from user.views import (
    CreateUserView,
    UserUpdateView,
    UserDeleteView
)

urlpatterns = [
    path('', CreateUserView.as_view(), name='user'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='userupdate'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='userdelete'),
]

from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserDetailAPIView,
    UserListAPIView
    )

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^details/$',UserListAPIView.as_view()),
    path('details/<int:pk>/',UserDetailAPIView.as_view()),
]
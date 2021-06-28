from django.conf.urls import url
# from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('resumes/',myresume,name='resumes'),
    path('profile_settings/',profilesettings,name='profilesettings'),
    path('practice/',practice,name='practice'),
]
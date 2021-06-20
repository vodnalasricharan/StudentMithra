from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    url(r'^create/$', NoteCreateAPIView.as_view(), name='create'),
    path('display/<int:pk>/',NoteDetailAPIView.as_view()),
]
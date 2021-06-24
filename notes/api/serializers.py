from notes.models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class NoteSerializer(ModelSerializer):
    class Meta:
        model=Note
        fields=['title','data']
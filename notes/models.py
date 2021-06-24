from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from django.conf import settings
# Create your models here.
class Note(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,blank=False)
    data=models.CharField(max_length=500,blank=True)
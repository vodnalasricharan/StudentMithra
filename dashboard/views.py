from django.shortcuts import render,redirect
from accounts.models import *
# Create your views here.

from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def myresume(request):
    return render(request,'dashoard.html')
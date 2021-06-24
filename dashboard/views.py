from django.shortcuts import render,redirect
from accounts.models import *
# Create your views here.

from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    return render(request,'dashboard.html')
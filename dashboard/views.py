from django.shortcuts import render
from accounts.models import *

# Create your views here.
def dashboard(request):
    return render(request,'profile.html')
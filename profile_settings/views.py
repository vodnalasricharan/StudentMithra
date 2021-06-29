from django.shortcuts import render,redirect
from accounts.models import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
from dashboard.forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def profilesettings(request):
    instance=Account.objects.get(user=request.user)
    form=AccountForm(instance=instance)
    if request.method=='POST':
        if form.is_valid():
            form.save()
    context={
        'title': 'profilesettings',
        'form': form,
        'instance': instance,
    }
    return render(request,'personal.html',context=context)

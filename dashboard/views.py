from django.shortcuts import render,redirect
from accounts.models import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


from django.core.exceptions import ValidationError
# Create your models here.
def validate_file(file):
    value= str(file.name)
    if value.endswith(".pdf") != True and value.endswith(".doc") != True and value.endswith(".docx") != True:
        raise ValidationError("Only PDF and Word Documents can be uploaded")
    file_size = file.size
    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)
    else:
        return value

from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    account=Account.objects.get(user=request.user)
    try:
        resume1=Resume.objects.get(slug=account.slug1)
    except ObjectDoesNotExist:
        resume1=None
    try:
        resume2=Resume.objects.get(slug=account.slug2)
    except ObjectDoesNotExist:
        resume2=None
    try:
        resume3=Resume.objects.get(slug=account.slug3)
    except ObjectDoesNotExist:
        resume3=None
    context={
        'resume1':resume1,
        'resume2': resume2,
        'resume3': resume3,
    }
    return render(request,'dashboard.html',context=context)

@login_required
def myresume(request):
    if request.method == 'POST':
        try:
            if request.POST.get("form_type") == 'resume1' and request.FILES['resume1']:
                myfile = request.FILES['resume1']
                try:
                    validate_file(myfile)
                except ValidationError:
                    messages.info(request,'only pdf/doc/docx files allowed')
                    return render(request, 'Resume.html')
                # fs = FileSystemStorage()
                # filename = fs.save(myfile.name, myfile)
                # uploaded_file_url = fs.url(filename)
                account=Account.objects.get(user=request.user)
                r1,create=Resume.objects.get_or_create(
                    slug=account.slug1,
                    user=account.user,
                )
                r1.resume=myfile
                r1.user=account.user
                r1.save()
                messages.success(request,'Resume1 was upadted with '+myfile.name)
                return render(request,'Resume.html')
            elif request.POST.get("form_type") == 'resume2' and request.FILES['resume2']:
                myfile = request.FILES['resume2']
                try:
                    validate_file(myfile.name)
                except ValidationError:
                    messages.info(request,'only pdf/doc/docx files allowed and max file size is 2MB')
                    return render(request, 'Resume.html')
                # fs = FileSystemStorage()
                # filename = fs.save(myfile.name, myfile)
                # uploaded_file_url = fs.url(filename)
                account=Account.objects.get(user=request.user)
                r1, create = Resume.objects.get_or_create(
                    slug=account.slug2,
                    user=account.user,
                )
                r1.resume = myfile
                r1.save()
                messages.success(request,'Resume2 was upadted with '+myfile.name)
                return render(request,'Resume.html')
            elif request.POST.get("form_type") == 'resume3' and request.FILES['resume3']:
                myfile = request.FILES['resume3']
                try:
                    validate_file(myfile.name)
                except ValidationError:
                    messages.info(request,'only pdf/doc/docx files allowed')
                    return render(request, 'Resume.html')
                # fs = FileSystemStorage()
                # filename = fs.save(myfile.name, myfile)
                # uploaded_file_url = fs.url(filename)
                account=Account.objects.get(user=request.user)
                r1, create = Resume.objects.get_or_create(
                    slug=account.slug3,
                    user=account.user,
                )
                r1.resume = myfile
                r1.save()
                messages.success(request,'Resume3 was upadted with '+myfile.name)
                return render(request,'Resume.html')
            else:
                messages.info(request,'Something went wrong please try again')
                return render(request,'Resume.html')
        except:
            messages.info(request, 'Something went wrong please try again')
            return render(request, 'Resume.html')

    return render(request,'Resume.html')

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
    return render(request,'profile.html',context=context)
from django.shortcuts import render,redirect
from accounts.models import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.

from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def myresume(request):
    if request.method == 'POST':
        if request.POST.get("form_type") == 'resume1' and request.FILES['resume1']:
            myfile = request.FILES['resume1']
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
            messages.success(request,'Resume1 was upadted with'+myfile.name)
            return render(request,'Resume.html')
        elif request.POST.get("form_type") == 'resume2' and request.FILES['resume2']:
            myfile = request.FILES['resume2']
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
            messages.success(request,'Resume2 was upadted with'+myfile.name)
            return render(request,'Resume.html')
        elif request.POST.get("form_type") == 'resume3' and request.FILES['resume3']:
            myfile = request.FILES['resume3']
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
            messages.success(request,'Resume3 was upadted with'+myfile.name)
            return render(request,'Resume.html')
        else:
            messages.info(request,'Something went wrong please try again')
            return render(request,'Resume.html')

    return render(request,'Resume.html')
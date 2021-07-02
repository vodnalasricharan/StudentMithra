from django.shortcuts import render,redirect
from accounts.models import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
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
    internships = Internship.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    try:
        education=Education.objects.get(user= request.user)
    except Education.DoesNotExist:
        education = None

    try:
        achieve=Addon.objects.get(user= request.user)
    except Addon.DoesNotExist:
        achieve = None

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
    # print(account.qr_code.url)
    coding_objs=codinglinks.objects.filter(user=request.user)
    context={
        'resume1':resume1,
        'resume2': resume2,
        'resume3': resume3,
        'account':account,
        'education':education,
        'achieve':achieve,
        'coding_objs':coding_objs,
        'internships':internships,
        'projects':projects,
        'others_view':False,
    }
    return render(request,'dashboard.html',context=context)

@login_required
def myresume(request):
    acc=Account.objects.get(user=request.user)
    res1=Resume.objects.filter(slug=acc.slug1).first()
    res2 = Resume.objects.filter(slug=acc.slug2).first()
    res3 = Resume.objects.filter(slug=acc.slug3).first()
    if request.method == 'POST':
        try:
            print(request.POST.get("form_type"))
            if request.POST.get("form_type") == 'resume1':
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
                return redirect('resumes')
            elif request.POST.get("form_type") == 'resume2':
                myfile = request.FILES['resume2']
                try:
                    validate_file(myfile)
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
                return redirect('resumes')
            elif request.POST.get("form_type") == 'resume3':
                myfile = request.FILES['resume3']
                try:
                    validate_file(myfile)
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
                return redirect('resumes')
            else:
                messages.info(request,'Something went wrong please try again')
                return redirect('resumes')
        except:
            messages.info(request, 'Something went wrong please try again')
            return redirect('resumes')
    context={
        'resume1':res1,
        'resume2':res2,
        'resume3':res3,
        'account':acc,
    }
    return render(request,'Resume.html',context)

@login_required
def practice(request):
    questions_incom=questions.objects.filter(user=request.user,status=False)
    questions_com=questions.objects.filter(user=request.user,status=True)
    context={
        'questions_incom':questions_incom,
        'questions_com':questions_com,
    }
    return render(request,'practice.html',context)

@login_required
def mark_as_completed(request,pk):
    instance = get_object_or_404(questions, id=pk)
    instance.status=True
    instance.save()
    messages.success(request, "Question is completed")
    return redirect('practice')
@login_required
def practice_completed(request):
    questions_incom = questions.objects.filter(user=request.user, status=False)
    questions_com = questions.objects.filter(user=request.user, status=True)
    context = {
        'questions_incom': questions_incom,
        'questions_com': questions_com,
    }
    return render(request, 'practice_comp.html', context)

@login_required
def practice_reset(request):
    questions.objects.filter(user=request.user).update(status=False)
    messages.info(request,'Questions have been reset')
    return redirect('practice')


@login_required
def practice_none(request):
    messages.info(request,'Link doesnot exists')
    return redirect(request.META.get('HTTP_REFERER'))


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


#*************************************************************standard blogs**********************************************************************

@login_required
def dsaimportant(request):
    return render(request,'dsaimport.html')
@login_required
def pathtoproduct(request):
    return render(request,'pathtoproduct.html')

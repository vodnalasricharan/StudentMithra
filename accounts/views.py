from django.shortcuts import render,redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
import random
from .forms import *
from django.contrib import messages
from .models import *
# Create your views here.
from dashboard.views import *
from .question_list import *
from itertools import islice
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.images import ImageFile
from django.core.files import File
from wsgiref.util import FileWrapper
# import magic
from django.http import HttpResponse, HttpResponseRedirect, Http404
import mimetypes
import pyqrcode
import png
from pyqrcode import QRCode


def authenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('dashboard')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func


@authenticated_user
def homepage(request):
    account = Account.objects.all()

    context = {'accounts':account,}
    return render(request,'homepage.html',context)

@authenticated_user
def accountregister(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.username = request.POST.get('username')
            form.email = request.POST.get('email')
            form.password1 = request.POST.get('password1')
            form.password2 = request.POST.get('password2')
            user = form.save()
            username = request.POST.get('username')
            try:
                for obj in questions_list:
                    questions.objects.create(user=user,ques=obj[0],ques_link=obj[1],video=obj[2],gfg=obj[3],status=False)
                url = pyqrcode.create('https://'+str(request.META['HTTP_HOST']+'/'+str(username)))
                print(url)
                url.png(settings.MEDIA_ROOT+'/'+str(username)+'.png',scale=8)
                print('qr_code created')
                obj_a=Account.objects.create(
                    user=user,
                    name=request.POST.get('username'),
                    email=request.POST.get('email'),
                    slug1=''.join(
                        random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for x in
                        range(10)),
                    slug2=''.join(
                        random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for x in
                        range(10)),
                    slug3=''.join(
                        random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for x in
                        range(10)),
                )
                print('account created')
                with open(settings.MEDIA_ROOT+'/'+str(username)+'.png', 'rb') as f:  # use 'rb' mode for python3
                    data = File(f)
                    obj_a.qr_code.save(str(username)+'.png', data, True)
                obj_a.save()

                messages.success(request, 'Account was created for ' + username)

                return redirect('login')
            except:
                messages.info(request,'something went wrong')

            else:
                messages.info(request,'something went wrong')
        else:
            messages.info(request,'enter correct details/user already exists')


    context = {'form': form}
    return render(request, 'register.html', context)

@authenticated_user
def accountlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.info(request, 'Username/Password is INCORRECT ')

    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect("login")


def othersprofile(request,pk):
    user=User.objects.get(username=pk)
    account = Account.objects.get(user=user)
    internships = Internship.objects.filter(user=user)
    projects = Project.objects.filter(user=user)
    try:
        education = Education.objects.get(user=user)
    except Education.DoesNotExist:
        education = None

    try:
        achieve = Addon.objects.get(user=user)
    except Addon.DoesNotExist:
        achieve = None

    try:
        resume1 = Resume.objects.get(slug=account.slug1)
    except ObjectDoesNotExist:
        resume1 = None
    try:
        resume2 = Resume.objects.get(slug=account.slug2)
    except ObjectDoesNotExist:
        resume2 = None
    try:
        resume3 = Resume.objects.get(slug=account.slug3)
    except ObjectDoesNotExist:
        resume3 = None

    coding_objs = codinglinks.objects.filter(user=user)
    context = {
        'resume1': resume1,
        'resume2': resume2,
        'resume3': resume3,
        'account': account,
        'education': education,
        'achieve': achieve,
        'coding_objs': coding_objs,
        'internships': internships,
        'projects': projects,
        'others_view': True,
    }
    return render(request, 'dashboard.html', context=context)


def get_resume(request,slug):
    try:
        resume=Resume.objects.get(slug=slug)
        return redirect(resume.resume.url)
    except Resume.DoesNotExist:
        resume=None
        context={
            'resume':resume,
        }
        return render(request,'show_resume.html',context)


def download_qr(request,pk):
    acc=Account.objects.get(id=pk)
    img = acc.qr_code
    if os.path.exists(img.file.name):
        with open(img.file.name,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition'] ='inline;filename='+os.path.basename(img.file.name)
            return  response
    else: Http404
    # wrapper = FileWrapper(open(img.file.name))  # img.file returns full path to the image
    # content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    # response = HttpResponse(wrapper, content_type=content_type)
    # response['Content-Length'] = os.path.getsize(img.file)
    # response['Content-Disposition'] = "attachment; filename=%s" % img.name
    # return response


"""def login_view(request):
    # print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    try:
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect("/")
        else:
            return render(request, "form.html", context={"form": form, "title": title})
    except:
        return render(request, "form.html", context={"form":form, "title": title})


def register_view(request):
    # print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("home")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)
"""


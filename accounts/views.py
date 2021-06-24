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
# def accountregister(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.username = request.POST.get('username')
#             form.email = request.POST.get('email')
#             form.password1 = request.POST.get('password1')
#             form.password2 = request.POST.get('password2')
#             user = form.save()
#             username = form.cleaned_data.get('username')
#
#             Account.objects.create(
#                 user=user,
#                 name= request.POST.get('username'),
#                 email = request.POST.get('email'),
#                 slug1=''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for x in range(10)),
#                 slug2=''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for x in range(10)),
#                 slug3=''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for x in range(10)),
#             )
#
#             messages.success(request, 'Account was created for ' + username)
#
#             return redirect('studentregister')
#
#     context = {'form': form}
#     return render(request, 'Registration.html', context)

#
# def accountlogin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')
#
#         else:
#             messages.info(request, 'Username OR password is incorrect')
#
#     context = {}
#     return render(request, 'AccountLogin.html', context)
#
# def logout_view(request):
#     logout(request)
#     return redirect("/")


def login_view(request):
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
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
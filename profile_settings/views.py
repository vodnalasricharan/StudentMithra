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
    try:
        profile = request.user.account
    except Account.DoesNotExist:
        profile = Account(user=request.user)

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AccountForm(instance=profile)
    context = {
        'title': 'create',
        'form': form,
    }
    return render(request, 'personal.html', context=context)

@login_required
def education_settings(request):
    try:
        profile = request.user.education
    except Education.DoesNotExist:
        profile = Education(user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully saved Education details")
            return redirect('dashboard')

    else:
        form = EducationForm(instance=profile)

    context = {'form': form,
               'title':'Create education',}
    return render(request, 'education.html', context=context)

# ********************************************************************* INTERNSHIPS *********************************************************************

@login_required
def internships(request):
    internships = Internship.objects.filter(user=request.user)
    context = {'internships': internships,
               'title': "Internships",
               }

    return render(request, 'intern_list.html', context)


@login_required
def add_internship(request):
    form = InternshipForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        return redirect('internships')
    context = {
        "form": form,
        "title": "Add Internship",
        "update":False,
    }
    return render(request, "intern_form.html", context)

@login_required
def update_intern(request,pk):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    internship= Internship.objects.get(id=pk)
    form= InternshipForm(request.POST or None,instance=internship)

    if request.method=="POST":
        form=InternshipForm(request.POST or None,instance=internship)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect('internships')
        else:
            messages.info(request, "something went wrong")

    context={'form':form,
             "title": "Update Internship",
             "update":True,
             'internship':internship,
             }
    return render(request,'intern_form.html',context)

@login_required
def delete_intern(request,pk):

    instance = get_object_or_404(Internship, id=pk)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect('internships')

# ********************************************************************* PROJECTS *********************************************************************

@login_required
def projects(request):
    projects = Project.objects.filter(user=request.user)
    context = {'projects': projects,
               'title': "Project",
               }

    return render(request, 'project.html', context)

@login_required
def add_project(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"Project Added")
        return redirect('projects')
    context = {
        "form": form,
        "title": "Add Project",
        "update":False,
    }
    return render(request, "project_form.html", context)

@login_required
def update_project(request,pk):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    project= Project.objects.get(id=pk)
    form= ProjectForm(request.POST or None,instance=project)

    if request.method=="POST":
        form=ProjectForm(request.POST or None,instance=project)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect('projects')
        else:
            messages.info(request, "something went wrong")

    context={'form':form,
             "title": "Update Project",
             "project":project,
             "update":True,
             }
    return render(request,'project_form.html',context)

@login_required
def delete_project(request,pk):

    instance = get_object_or_404(Project, id=pk)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect('projects')



# ********************************************************************* ACHIEVEMENTS *********************************************************************


@login_required
def achievements(request):
    try:
        profile = request.user.addon
    except Addon.DoesNotExist:
        profile = Addon(user=request.user)
    if request.method == 'POST':
        form = AddonForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully saved Education details")
            return redirect('dashboard')

    else:
        form = AddonForm(instance=profile)

    context = {'form': form,
               'title': 'Apply Changes', }
    return render(request, 'achievements.html', context=context)


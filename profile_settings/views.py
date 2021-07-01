from django.shortcuts import render,redirect
from accounts.models import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
from dashboard.forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
# Create your views here.

@login_required
def profilesettings(request):
    try:
        profile = request.user.account
    except Account.DoesNotExist:
        profile = Account(user=request.user)

    if request.method == 'POST':
        form = AccountForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AccountForm(request.POST or None,request.FILES or None,instance=profile)
    context = {
        'title': 'Update',
        'form': form,
        'profile':profile,
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
            messages.success(request, "Successfully saved Achievement details")
            return redirect('dashboard')

    else:
        form = AddonForm(instance=profile)

    context = {'form': form,
               'title': 'Apply Changes', }
    return render(request, 'achievements.html', context=context)

#************************************************************************** coding profiles ******************************************************************

@login_required
def coding(request):
    c_links=codinglinks.objects.filter(user=request.user)

    context = {'c_links': c_links,
               'title': "Coding Profiles",
               }
    return render(request,'coding_profiles.html',context)

@login_required
def add_coding(request):
    form = CodingForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            inst = form.save(commit=False)
            inst.user=request.user
            if inst.platform == 'leetcode' :
                inst.image=static('/assets/img/7xInX10u_400x400.jpg')
            elif inst.platform == 'hackerrank':
                inst.image = static('/assets/img/HackerRank_Icon-1000px.png')
            elif inst.platform == 'codechef':
                inst.image = static('/assets/img/codechef.png')
            elif inst.platform == 'codeforces':
                inst.image = static('/assets/img/codeforces.jpg')
            elif inst.platform == 'gfg' :
                inst.image = static('/assets/img/QNHrwL2q.jpg')
            else:
                inst.image = static('/assets/img/0f8b2870896edcde8f6149fe2733faaf.jpg')

            inst.save()
            messages.success(request,'succesfully added')
            return redirect('coding_links')

    context = {
        "form": form,
        "title": "Add Coding Links",
        "update": False,
    }
    return render(request,'coding_form.html',context)


@login_required
def update_coding(request,pk):
    c_link=codinglinks.objects.get(id=pk)
    form = CodingForm(request.POST or None, instance=c_link)
    if request.method == "POST":
        if form.is_valid():
            inst = form.save(commit=False)
            inst.user = request.user
            if inst.platform == 'leetcode':
                inst.image = 'https://drive.google.com/file/d/11CleozRxg2utNLDoTFLd_92H53wjvxlL/view?usp=sharing'
            elif inst.platform == 'hackerrank':
                inst.image = 'https://drive.google.com/file/d/1wu3Wh6iJ3maAoaTT0hCm5PprhMvusRSA/view?usp=sharing'
            elif inst.platform == 'codechef':
                inst.image = 'https://drive.google.com/file/d/1_W8Q3zgGHqKqJJzlI-oY7mz4w8wypisq/view?usp=sharing'
            elif inst.platform == 'codeforces':
                inst.image = 'https://drive.google.com/file/d/1bEuT-de5ikzQeVBqKJxViadhz6Rfr2DQ/view?usp=sharing'
            elif inst.platform == 'gfg':
                inst.image = 'https://drive.google.com/file/d/18F4Nj_pUZ9aAhow5qScjUdwhYQ5_uJG7/view?usp=sharing'
            else:
                inst.image = 'https://drive.google.com/file/d/1cb5OVf5XxRkyktRpsfnXfn_xtNclo5gq/view?usp=sharing'

            inst.save()
            messages.success(request, 'succesfully updated')
            return redirect('coding_links')

    context = {
        "form": form,
        "title": "Update Coding Links",
        "update": True,
        "c_link":c_link,
    }
    return render(request, 'coding_form.html', context)

@login_required
def delete_coding(request,pk):
    instance=get_object_or_404(codinglinks,id=pk)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect('coding_links')
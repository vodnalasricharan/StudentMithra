from django.shortcuts import render,redirect

from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def note_create(request):
    form = NoteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        return redirect('noteslist')
    context = {
        "form": form,
        "title": "Create Note",
    }
    return render(request, "note_form.html", context)

@login_required
def list_of_notes(request):

    notes = Note.objects.filter(user=request.user)
    context = {'notes':notes,
               'title':"Notes",
               }

    return render(request,'notes.html',context)


@login_required
def update_note(request,pk):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    note= Note.objects.get(id=pk)
    form= NoteForm(request.POST or None,instance=note)

    if request.method=="POST":
        form=NoteForm(request.POST or None,instance=note)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect('noteslist')
        else:
            messages.info(request, "something went wrong")

    context={'form':form,
             "title": "Update Notes",
             }
    return render(request,'note_form.html',context)

@login_required
def note_delete(request,pk):

    instance = get_object_or_404(Note, id=pk)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect('noteslist')
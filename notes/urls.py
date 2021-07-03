from django.conf.urls import url

from django.urls import path

from .views import *



urlpatterns = [
    url(r'^$', list_of_notes, name='noteslist'),
    path('createnote/',note_create,name='createnote'),
    url(r'^(?P<pk>[\w-]+)/edit/$', update_note, name='updatenote'),
    url(r'^(?P<pk>[\w-]+)/delete/$', note_delete,name='deletenote'),


]
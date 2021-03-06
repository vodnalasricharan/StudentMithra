from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns=[
    path('', profilesettings, name='profilesettings'),
    path('education/',education_settings,name='edu_settings'),


    path('internships',internships,name='internships'),
    path('addinternship/',add_internship,name='addintern'),
    url(r'^(?P<pk>[\w-]+)/edit/$', update_intern, name='intern_update'),
    url(r'^(?P<pk>[\w-]+)/delete/$', delete_intern,name='intern_delete'),


    path('projects/',projects,name='projects'),
    path('addprojects/',add_project,name='add_project'),
    url(r'^(?P<pk>[\w-]+)/update/$', update_project, name='update_project'),
    url(r'^(?P<pk>[\w-]+)/deleteproj/$', delete_project,name='delete_project'),


    path('achievements/',achievements,name='achievements'),
    path('coding_links/',coding,name='coding_links'),
    path('add_coding_links',add_coding,name='add_coding'),
    path('update_coding_links/<int:pk>/',update_coding,name='update_coding'),
    path('delete_coding_links/<int:pk>/',delete_coding,name='delete_coding'),
    ]
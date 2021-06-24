"""studentmithra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from accounts.views import *
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',homepage,name='home'),
    # path('profile/',profile_view,name='profile'),
    path('dashboard/',dashboard,name='dashboard'),
    url(r'^api/users/', include(("accounts.api.urls",'userapi'),namespace='userapi')),
    path('login/',accountlogin,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',accountregister,name='register'),
    url(r'^api/posts/', include(("posts.api.urls",'posts-api'), namespace='posts-api')),
    path('posts/',include('posts.urls')),
    url(r'^api/comments/', include(("comments.api.urls",'comments-api'), namespace='comments-api')),
    url(r'^comments/', include(("comments.urls",'comments'), namespace='comments')),
    url(r'^api/notes/', include(("notes.api.urls",'posts-api'), namespace='notes-api')),
    # url(r'^notes/',include(("notes.urls",'notes'),namespace='notes')),
]

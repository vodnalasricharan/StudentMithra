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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as  auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',homepage,name='home'),
    # path('profile/',profile_view,name='profile'),
    path('dashboard/',include('dashboard.urls')),
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
    path('notes/',include('notes.urls')),
    path('profile_settings/',include('profile_settings.urls')),
    path('resume/<str:slug>/',get_resume,name='showresume'),
    path('user/<str:pk>', othersprofile, name='othersprofile'),

    path('download_qr/<int:pk>',download_qr,name='download_qr'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),

    path("contact", contact, name="contact"),
    url(r'^changepassword/$', change_password , name='change_password')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


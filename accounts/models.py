from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from phone_field import PhoneField
# Create your models here.
def validate_image(image):
    file_size = image.file.size
    # limit_kb = 150
    # if file_size > limit_kb * 1024:
    #     raise ValidationError("Max size of file is %s KB" % limit)

    limit_mb = 1
    if file_size > limit_mb * 1024 * 1024:
       raise ValidationError("Max size of file is %s MB" % limit_mb)

class Account(models.Model):
    GEN= (
        ('male', 'male'),
        ('female', 'female'),
    )
    user= models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    # we set null=True just for any other exception errors..but this name field cannot be empty
    email = models.CharField(max_length=200, null=True, validators=[validate_email])
    date_created = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    gender = models.CharField(choices=GEN,max_length=10,blank=True,null=True)
    # profile_pic = models.ImageField(null=True, default='default.png', validators=[validate_image],upload_to='profilepics')
    mobile_no= PhoneField(blank=True, help_text='Contact phone number')
    slug1 = models.CharField(max_length=20,blank=True,unique=True,null=True)
    slug2 = models.CharField(max_length=20, blank=True,unique=True,null=True)
    slug3 = models.CharField(max_length=20, blank=True,unique=True,null=True)

    def __str__(self):
        return self.email

class Resume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.CharField(max_length=20,null=False,unique=True)
    resume=models.FileField(upload_to='pdfs')

    def __str__(self):
        return self.slug

class codinglinks(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    link=models.URLField(max_length=500,null=False)
    def __str__(self):
        return self.link

class Internship(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=50,null=False)
    Organisation=models.CharField(max_length=100,null=False)
    discription=models.CharField(max_length=1000,null=False)

class Project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=False)
    link=models.URLField(max_length=500,null=True,blank=True)
    discription=models.CharField(max_length=1000,null=False)

class Addon(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    discription=models.CharField(max_length=500,null=False)
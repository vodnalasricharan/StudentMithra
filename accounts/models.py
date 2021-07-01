from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
# Create your models here.
def validate_file(file):
    value= str(file.name)
    if value.endswith(".pdf") != True and value.endswith(".doc") != True and value.endswith(".docx") != True:
        raise ValidationError("Only PDF and Word Documents can be uploaded")
    file_size = file.size
    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)
    else:
        return value
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
    profile_pic = models.ImageField(null=True, default='default.png', validators=[validate_image],upload_to='profilepics')
    mobile_no= PhoneNumberField(blank=True)
    slug1 = models.CharField(max_length=20,blank=True,unique=True,null=True)
    slug2 = models.CharField(max_length=20, blank=True,unique=True,null=True)
    slug3 = models.CharField(max_length=20, blank=True,unique=True,null=True)
    address=models.CharField(max_length=200,blank=True,null=True)
    linkedin_profile=models.URLField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.email

class Resume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.CharField(max_length=20,null=False,unique=True)
    resume=models.FileField(upload_to='pdfs',validators=[validate_file])

    def __str__(self):
        return self.slug

class codinglinks(models.Model):
    PLT=(
        ('leetcode','Leetcode'),
        ('hackerrank','Hackerrank'),
        ('codechef','Codechef'),
        ('codeforces','Codeforces'),
        ('gfg','GeeksForGeeks'),
        ('other','Other'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    platform=models.CharField(choices=PLT,max_length=200,default='leetcode')
    link=models.URLField(max_length=500)
    def __str__(self):
        return self.platform

class Internship(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=50,null=False)
    Organisation=models.CharField(max_length=100,null=False)
    description=models.CharField(max_length=1000,null=False)

    def __str__(self):
        return self.role

class Project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=False)
    link=models.URLField(max_length=500,null=True,blank=True)
    description=models.CharField(max_length=1000,null=False)

    def __str__(self):
        return self.title

class Addon(models.Model):
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    Achievements=models.CharField(max_length=500,default='-')

class Education(models.Model):
    QUA=(
        ('Bachelors','Bachelor'),
        ('Masters','master'),
        ('Diploma','diploma'),
        ('Degree','degree'),
        ('HighSchool','highschool'),
    )
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    inst_name=models.CharField(max_length=200)
    yop=models.IntegerField(default=2000)
    qualif=models.CharField(choices=QUA,max_length=200,default='highschool')
    branch=models.CharField(max_length=200,blank=True,null=True)


    def __str__(self):
        return self.inst_name


class questions(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ques=models.CharField(max_length=300,blank=True,null=True)
    ques_link=models.URLField(max_length=500,blank=True,null=True)
    video=models.URLField(max_length=500,blank=True,null=True)
    gfg=models.URLField(max_length=500,blank=True,null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)+' : '+str(self.ques)


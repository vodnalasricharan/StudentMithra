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
    user= models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    # we set null=True just for any other exception errors..but this name field cannot be empty
    email = models.CharField(max_length=200, null=True, validators=[validate_email])
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # profile_pic = models.ImageField(null=True, default='default.png', validators=[validate_image],upload_to='profilepics')
    mobile_no= PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.email

from django import forms
from accounts.models import *
from phone_field import PhoneField
class AccountForm(forms.ModelForm):
    mobile_no=PhoneField()
    class Meta:
        model=Account
        fields=[
            'gender',
            'address',
            'mobile_no',
            'linkedin_profile',
        ]

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields=[
            'inst',
            'yop',
            'qualif',
            'branch',
        ]

class InternshipForm(forms.ModelForm):
    class Meta:
        model=Internship
        fields=[
            'role',
            'organisation',
            'discription',
        ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=[
            'title',
            'link',
            'discription',
        ]

class AddonForm(forms.ModelForm):
    class Meta:
        model=Addon
        fields=[
            'discription',
        ]

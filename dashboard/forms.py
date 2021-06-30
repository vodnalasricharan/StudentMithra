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
            'inst_name',
            'yop',
            'qualif',
            'branch',
        ]

class InternshipForm(forms.ModelForm):
    class Meta:
        model=Internship
        fields=[
            'role',
            'Organisation',
            'description',
        ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=[
            'title',
            'link',
            'description',
        ]

class AddonForm(forms.ModelForm):
    Achievements = forms.CharField(widget=forms.Textarea(attrs={'style': 'height:150px;width:700px'}))
    class Meta:
        model=Addon
        fields=[
            'Achievements',
        ]


from django import forms
from accounts.models import *
from phone_field import PhoneField
class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=[
            'full_name',
            'email',
            'gender',
            'address',
            'mobile_number',
            'linkedin_profile',
            'github',
            'profile_pic',
        ]

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields=[
            'institute_name',
            'year_of_pass',
            'highest_degree',
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
class CodingForm(forms.ModelForm):
    class Meta:
        model=codinglinks
        fields=[
            'platform',
            'link',
        ]

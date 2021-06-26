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
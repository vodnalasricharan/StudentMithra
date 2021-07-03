from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
class CreateUserForm(UserCreationForm):
	username = forms.CharField(error_messages={'required': 'Please specify your username'})
	email = forms.CharField(error_messages={'required': 'Email is a required field'})
	password1 = forms.CharField(error_messages={'required': 'Password is a required field'})
	password2 = forms.CharField(error_messages={'required': 'Repeat Password is a required field'})

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2


User = get_user_model()


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		# user_qs = User.objects.filter(username=username)
		# if user_qs.count() == 1:
		#     user = user_qs.first()
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect passsword")
			if not user.is_active:
				raise forms.ValidationError("This user is not longer active.")
		return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email address')
	email2 = forms.EmailField(label='Confirm Email')
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password'
		]


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea(attrs={'rows': 8, 'cols': 25}))
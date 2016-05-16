from django import forms
from .models import UserProfile
from django.contrib.auth import (
	authenticate, 
	get_user_model, 
	login, 
	logout,
	)

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Username does not exist.")
			if not user.check_password(password):
				raise ValidationError("Incorrect password!")
			if not user.is_active:
				raise forms.ValidationError("This user no longer has an active account.")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
	email = forms.EmailField(label="Email Address")
	email_verify = forms.EmailField(label="Confirm Email")
	password = forms.CharField(widget=forms.PasswordInput)
	password_verify = forms.CharField(widget=forms.PasswordInput)
	first_name = forms.CharField(label="First Name")
	last_name = forms.CharField(label="Last Name")
	# description = forms.TextField(max_length=1000)
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'email_verify',
			'password',
			'password_verify',
		]
	def clean(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		email_verify = self.cleaned_data.get("email_verify")
		password = self.cleaned_data.get("password")
		password_verify = self.cleaned_data.get("password_verify")
		if email != email_verify:
			raise forms.ValidationError("Emails must match.")
		if password != password_verify:
			raise forms.ValidationError("Passwords do not match.")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has alrerady been registered.")
		return super(UserRegistrationForm, self).clean(*args, **kwargs)


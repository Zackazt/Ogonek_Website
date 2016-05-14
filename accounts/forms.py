from django import forms
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
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email_verify',
			'password',
		]
	def clean(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		email_verify = self.cleaned_data.get("email_verify")
		if email != email_verify:
			raise forms.ValidationError("Emails must match.")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has alrerady been registered.")
		return super(UserRegistrationForm, self).clean(*args, **kwargs)

from django.shortcuts import render, redirect
from django.contrib.auth import (
	authenticate, 
	get_user_model, 
	login, 
	logout,
	)
from .forms import UserLoginForm, UserRegistrationForm
# Create your views here.
def login_view(request):
	on_page = request.GET.get('on_page')
	print(on_page)
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		username = username
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		if on_page == "/register/":
			return redirect("/")
		if on_page != request.path:
			return redirect(on_page)
		else:
			return redirect("/")
	context = {
		"form": form,
		"title": title,
	}
	return render(request, "form.html", context)

def register_view(request):
	on_page = request.GET.get('on_page')
	print(on_page)
	title = "Register"
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		username = username
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=username, password=password)
		login(request, new_user)
		if on_page == "/login/":
			return redirect("/")
		if on_page != request.path:
			return redirect(on_page)
		else:
			return redirect("/")
	context = {
		"form": form,
		"title": title,
	}
	return render(request, "form.html", context)

def logout_view(request):
	on_page = request.GET.get('on_page')
	logout(request)
	if on_page != request.path:
			return redirect(on_page)
	else:
		return redirect("/")
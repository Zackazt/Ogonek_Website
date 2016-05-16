from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def userprofile_view(request):
	url = request.path
	username = url.split('/')[-1]
	which_user = get_object_or_404(User, username=username)
	if which_user:
		context = {
			"username_destination": username,
			"which_user": which_user,
		}
		return render(request, "profile.html", context)
	else:
		raise Http404

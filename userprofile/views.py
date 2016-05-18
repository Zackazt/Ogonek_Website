from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post 
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


# Create your views here.
def userprofile_view(request):
	url = request.path
	if url is not None:
		username = url.split('/')[-1]
		which_user = get_object_or_404(User, username=username)
		user_posts = Post.objects.filter(user=which_user).order_by('-timestamp')
	if which_user:
		context = {
			"username_destination": username,
			"which_user": which_user,
			"user_posts": user_posts,
		}
		return render(request, "profile.html", context)
	else:
		raise Http404

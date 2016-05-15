from django.conf.urls import url
from django.contrib import admin

from .views import userprofile_view

urlpatterns = [
	url(r'^[\w-]', userprofile_view),
]
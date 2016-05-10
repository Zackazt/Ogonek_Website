from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
	# If I forget what these do,
	# Refer to: https://docs.djangoproject.com/en/1.9/ref/contrib/admin/
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["title"] 
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "body"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
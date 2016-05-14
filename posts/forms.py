from django import forms
from .models import Post



class PostForm(forms.ModelForm):
	genre_list = (
			('Opinion', 'Opinion'), 
			('Lifestyle', 'Lifestyle'),
			('History', 'History'),
			('Health', 'Health'),
			('Technology', 'Technology'),
			('Science', 'Science'),
			('Music', 'Music'),
			('Art', 'Art'),
			('Social', 'Social'),
		)
	publish = forms.DateField(widget=forms.SelectDateWidget)
	genre = forms.ChoiceField(choices=genre_list)
	class Meta:
		model = Post
		fields = [
			"title",
			"image",
			"body",
			"draft",
			"publish",
			"genre",
		]
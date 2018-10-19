from django.shortcuts import render
from django.http import HttpResponse
from .models import Post   #because models is in same dir .model is used


# Create your views here.

# templates for our blog are in templates folder 
# blog -> templates -> blog -> template.html

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context) #context is now accesible in .html page


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})


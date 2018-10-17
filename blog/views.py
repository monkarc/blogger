from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# templates for our blog are in templates folder 
# blog -> templates -> blog -> template.html



def home(request):
	return render(request, 'blog/home.html')


def about(request):
	return HttpResponse('<h1>Blog About Page</h1>')


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# templates for our blog are in templates folder 
# blog -> templates -> blog -> template.html

posts=[
{
	'author':'John doe',
	'title':'Blog Post 1',
	'content':'First post contents',
	'date_posted':'2018-10-17'
},
{
	'author':'Jane doe',
	'title':'Blog Post 2',
	'content':'Second post contents',
	'date_posted':'2018-10-18'
}

]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context) #context is now accesible in .html page


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})


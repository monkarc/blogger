from django.shortcuts import render
from django.views.generic import ListView, DetailView
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


# class based views look for certain template with naming convention
# The naming convention is <app>/<model>_<viewtype>.html
# when template with this name is unavailable, \
#  we can then redirect to already available template using 'template_name'
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


# DetailView looks for certain template with naming convention
# The naming convention is <app>/<model>_detail.html
class PostDetailView(DetailView):
    model = Post



def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})


# CLASS BASED VIEWS
# 1. update views
# 2. list views (blog, subscription on youtube)
# 3. detail views
# 4. create views
# 5. delete views
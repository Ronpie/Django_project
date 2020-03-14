from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
#function home
#handle traffic from homepage of our blog
#take the request argument
#function to render a template
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html',context)
#instead of '<doctype>...'
#we can using template to not repeting writing

def about(request):
	return render(request, 'blog/about.html',{'title':'About'})
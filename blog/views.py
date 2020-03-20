from django.shortcuts import render,get_object_or_404
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	DeleteView,
	UpdateView,
	)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
#function home
#handle traffic from homepage of our blog
#take the request argument
#function to render a template
# we have passed some information in function
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html',context)
#instead of '<doctype>...'
#we can using template to not repeting writing

#in class we just setting some variable
class PostListView(ListView):
	model = Post
	# browser look for the template
	# <app>/<model>_<viewtype>.html  default is -> blog/post_list.html
	template_name = 'blog/home.html'
	# we are setting the variable to pass in to html is 'posts'
	context_object_name = 'posts'
	# we want to see lasted post in the top. "-" reverse
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	# browser look for the template
	# <app>/<model>_<viewtype>.html  default is -> blog/post_list.html
	template_name = 'blog/user_posts.html'
	# we are setting the variable to pass in to html is 'posts'
	context_object_name = 'posts'
	# we want to see lasted post in the top. "-" reverse
	# when having get_query_set we don't need ordering
	# ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		#get username from url by self.kwargs.get('username')
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content'] 
	#sharing with update view then blog/post_form.html
	# we need to send the author for this process
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#but still not redirect page after create new post
	# we need to add method get_absolute_url as instruction in django web-brower erorrs
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title','content']
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#make sure that only the author is the one who can update, combine with UserPassesTestMixin
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html',{'title':'About'})

#list detail create delete update views 
#list: all of the blog post, or all list of subcribe video in youtube
#detail to each post or each video in list


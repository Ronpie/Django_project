from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			'''
			flash message just sent one time alert
			will disappear in next request
			messages.debug
			messages.info
			messages.success
			messages.warning
			messages.error
			'''
			messages.success(request,f'Account created for {username}!')
			return redirect('blog-home')
	else:
		form = UserRegisterForm()
	return render(request,'users/register.html',{'form':form})


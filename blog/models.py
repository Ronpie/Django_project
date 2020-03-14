from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	'''
	auto_now = True : update the time every time 
	the Post is updated
	auto_now_add = True: update only once 
	when the Post is created
	timezone.now don't have '()' because we don't
	want to execute that now
	'''
	date_posted = models.DateTimeField(default=timezone.now)
	#Foreign Key 
	#delete the user then delete the post together
	#but delete the post will just delete the post
	author = models.ForeignKey(User,on_delete=models.CASCADE)
 	
 	#to show the object we need
 	#dunder(__) str method
	def __str__(self):
  	  	return self.title






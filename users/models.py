from django.db import models
from django.contrib.auth.models import User
# After creating model 
# Remember to makemigrations, migrate
# Register to admin.py
class Profile(models.Model):
	# Delete user will delete the profile
	# but delete profile not delete user
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'


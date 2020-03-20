from django.db import models
from django.contrib.auth.models import User
from PIL import Image
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

	# Reduce image size to reduce file size saving on server 
	# Help improving the loading of site to user
	def save(self):
		super().save()

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

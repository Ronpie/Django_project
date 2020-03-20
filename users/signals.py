#signals to setting default stuff 
#now default image after user creation

#remember to add the signal declaration in to the apps.py

# The signal
from django.db.models.signals import post_save

# The sender 
from django.contrib.auth.models import User

# The receiver
from django.dispatch import receiver

from .models import Profile

#we want to run every one user is created
#we are using receiver decorator
#to let create_profile as a receiver
#Take all the argument the post_save signal pass to it
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()
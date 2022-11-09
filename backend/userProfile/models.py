from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg',upload_to='profile_images',related_name='avatar')

    bio = models.TextField()

    def __str__(self):
        return self.user.username

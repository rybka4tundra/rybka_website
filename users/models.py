from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default=static('profile_images/default/profile_image.jpg'), upload_to='profile_images')
    bio = models.TextField(blank=True)
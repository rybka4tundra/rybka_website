from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='users/profile_images/default.jpg', upload_to='users/profile_images')
    bio = models.TextField(blank=True)
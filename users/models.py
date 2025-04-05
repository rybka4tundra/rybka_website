from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='users/profile_images/default.jpg', upload_to='users/profile_images')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class FollowRelationship(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower')
    target = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='target')

    def __str__(self):
        return self.follower.user.username + '->' + self.target.user.username

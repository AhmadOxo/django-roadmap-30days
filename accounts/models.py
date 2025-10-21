from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=80, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

def avatar_upload_path(instance, filename):
    return f"avatars/user_{instance.user.id}/{filename}" 
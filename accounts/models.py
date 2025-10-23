from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=250, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_absolute_url(self):
        return f"/profile/{self.user.username}"
    

def avatar_upload_path(instance, filename):
    return f"avatars/user_{instance.user.id}/{filename}" 
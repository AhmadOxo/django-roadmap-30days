from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    note = models.ForeignKey(Notes, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=40)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comment by {self.author} on "{self.note}" at {self.published_at}'
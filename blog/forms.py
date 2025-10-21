from django import forms
from .models import Post, Comment


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your Comment...'})}
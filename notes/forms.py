from django import forms
from .models import Notes, Comment


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your comment...'}),
        }
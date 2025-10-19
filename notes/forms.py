from django import forms
from .models import Notes, Comment


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your comment...'}),
        }
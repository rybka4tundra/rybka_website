from django import forms
from django.forms import ModelForm
from .models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'date')
        help_texts = {
            'title': None,
            'content': None,
            'date': None
        }
        labels = {
            'title': '',
            'content': '',
            'date': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Content'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Date'}),
        }

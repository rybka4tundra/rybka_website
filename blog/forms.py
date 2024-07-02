from django import forms
from django.forms import ModelForm
from .models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'date')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control'})
        }

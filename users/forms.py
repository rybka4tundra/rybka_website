from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
            'username': None,
            'password': None
        }
        labels = {
            'username': '',
            'password': ''
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password'})
        }

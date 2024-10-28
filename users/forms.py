from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from users.models import Profile


class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
            'username': None,
            'password': None,
        }
        labels = {
            'username': '',
            'password': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password'})
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


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


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar')
        help_texts = {
            'bio': None,
            'avatar': None,
        }
        labels = {
            'avatar': '',
            'bio': '',
        }
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Avatar'}),
            'bio': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Bio'})
        }


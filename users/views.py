from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from blog.models import Post
from .forms import UserLoginForm, UserRegisterForm, ProfileEditForm
from .models import Profile


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login_user')
        else:
            messages.success(request, ('There was an Error during registration, try again.'))
            return redirect('register_user')
    else:
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'authentication/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ('There was an Error logging in, try again.'))
            return redirect('login_user')
    else:
        form = UserLoginForm
        context = {
            'form': form
        }
        return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You were successfully logged out!')
    return redirect('index')


def user_profile(request, username):
    profile = Profile.objects.get(user=User.objects.get(username=username))
    posts = Post.objects.filter(author=profile)
    context = {
        'profile': profile,
        'posts': posts
    }
    return render(request, 'profile/profile.html', context)


@login_required
def edit_user_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'You had successfully changed your profile!')
            return redirect('user_profile', username=request.user.username)
        else:
            messages.error(request, 'Please fill right data')
            return redirect('user_profile', username=request.user.username )
    else:
        form = ProfileEditForm(instance=profile)


        context = {
            'form': form
        }

        return render(request, "profile/edit_profile.html", context)

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from blog.models import Post
from .forms import UserLoginForm, UserRegisterForm, ProfileEditForm
from .models import Profile, FollowRelationship


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
    subscribers = [relationship.follower for relationship in FollowRelationship.objects.filter(target=profile)]
    if request.user.is_authenticated:
        is_subscribed = FollowRelationship.objects.filter(follower=Profile.objects.get(user=request.user),
                                                          target=profile).exists()
    else:
        is_subscribed = None
    context = {
        'profile': profile,
        'posts': posts,
        'subscribers': subscribers,
        'is_subscribed': is_subscribed
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
            return redirect('user_profile', username=request.user.username)
    else:
        form = ProfileEditForm(instance=profile)

        context = {
            'form': form
        }

        return render(request, "profile/edit_profile.html", context)


@login_required
def subscribe_to_profile(request, subscribe_to_profile_id):
    current_user_profile = Profile.objects.get(user=request.user)
    subscribe_to_profile = Profile.objects.get(id=subscribe_to_profile_id)
    FollowRelationship.objects.create(follower=current_user_profile, target=subscribe_to_profile)
    return redirect('user_profile', username=subscribe_to_profile.user.username)


@login_required
def unsubscribe_from_profile(request, unsubscribe_from_profile_id):
    current_user_profile = Profile.objects.get(user=request.user)
    unsubscribe_from_profile = Profile.objects.get(id=unsubscribe_from_profile_id)
    follow_relationship = FollowRelationship.objects.get(follower=current_user_profile, target=unsubscribe_from_profile)
    follow_relationship.delete()
    messages.success(request, f'You successfully unsubscribed from {unsubscribe_from_profile.user.username}!')
    return redirect('user_profile', username=unsubscribe_from_profile.user.username)

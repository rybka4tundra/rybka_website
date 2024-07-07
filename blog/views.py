from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


from .models import Post
from .forms import PostCreateForm


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "blog/index.html", context)


def about(request):
    return render(request, "blog/about.html", {})


def greet(request, name):
    return HttpResponse(f"<h1>Hello, {name.capitalize()}!</h1>")


def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You had successfully created a post!')
            return redirect('index')
    else:
        form = PostCreateForm
        context = {
            'form': form
        }
        return render(request, "blog/create_post.html", context)

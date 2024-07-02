from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from datetime import datetime


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

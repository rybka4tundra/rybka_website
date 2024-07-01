from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from datetime import datetime


def index(request):
    now = datetime.now()
    current_date = now.date()
    posts = Post.objects.all()
    context = {
        'current_date': current_date,
        'posts': posts
    }
    return render(request, "blog/index.html", context)


def about(request):
    return HttpResponse('<h1>About</h1>')


def greet(request, name):
    return HttpResponse(f"<h1>Hello, {name.capitalize()}!</h1>")

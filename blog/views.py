from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/index.html", context)


def about(request):
    return HttpResponse('<h1>About</h1>')


def greet(request, name):
    return HttpResponse(f"<h1>Hello, {name.capitalize()}!</h1>")

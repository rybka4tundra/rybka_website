from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def about(request):
    return HttpResponse('<h1>About</h1>')


def greet(request, name):
    return HttpResponse(f"<h1>Hello, {name.capitalize()}!</h1>")

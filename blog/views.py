from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the blog index</h1>")


def about(request):
    return HttpResponse('<h1>About</h1>')


def greet(request, name):
    return HttpResponse(f"<h1>Hello, {name.capitalize()}!</h1>")

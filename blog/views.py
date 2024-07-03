from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

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
    submitted = False
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_post/?submitted=True')
    else:
        form = PostCreateForm
        if 'submitted' in request.GET:
            submitted = True

        context = {
            'form': form,
            'submitted': submitted
        }
        return render(request, "blog/create_post.html", context)

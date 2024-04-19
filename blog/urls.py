from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="blog-about"),
    path("<str:name>", views.greet, name="greet")
]

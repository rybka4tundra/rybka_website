from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login_user"),
    #path("about/", views.about, name="about"),
    #path("<str:name>", views.greet, name="greet"),
    #path("create_post/", views.create_post, name="create-post")
]
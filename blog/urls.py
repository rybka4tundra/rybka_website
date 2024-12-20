from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("<str:name>", views.greet, name="greet"),
    path("create_post/", views.create_post, name="create-post"),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post')
]

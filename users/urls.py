from django.urls import path
from . import views
urlpatterns = [
    path("register_user", views.register_user, name="register_user"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("user_profile", views.user_profile, name="user_profile"),
    path("edit_user_profile", views.edit_user_profile, name="edit_user_profile")
]


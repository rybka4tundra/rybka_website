from django.urls import path
from . import views
urlpatterns = [
    path("register_user", views.register_user, name="register_user"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("user_profile/<str:username>", views.user_profile, name="user_profile"),
    path("edit_user_profile", views.edit_user_profile, name="edit_user_profile"),
    path("subscribe_to_profile/<int:subscribe_to_profile_id>", views.subscribe_to_profile, name="subscribe_to_profile"),
    path("unsubscribe_from_profile/<int:unsubscribe_from_profile_id>", views.unsubscribe_from_profile, name="unsubscribe_from_profile")
]


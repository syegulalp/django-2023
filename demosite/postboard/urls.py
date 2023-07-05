from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_form, name="login"),
    path("login_post", views.login_post, name="login_post"),
    path("new", views.post_new, name="post_new"),
    path("logout", views.logout_form, name="logout"),
]

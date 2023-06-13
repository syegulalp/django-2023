from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("t", views.template, name="template"),
    path("t/new", views.post_new, name="post_new"),
]

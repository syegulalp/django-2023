from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Post


def index(request):
    last_posts = Post.objects.order_by("-date")[:7]
    template = loader.get_template("index.html")
    context = {"last_posts": last_posts}
    return HttpResponse(template.render(context, request))


@login_required
def post_new(request):
    new_post_text = request.POST["text_input"]
    new_post = Post(post_text=new_post_text, user=request.user)
    new_post.save()
    return HttpResponseRedirect(reverse("index"))


def login_form(request):
    template = loader.get_template("login.html")
    context = {"message": "Please log in", "form": AuthenticationForm()}
    return HttpResponse(template.render(context, request))


def login_post(request):
    template = loader.get_template("login.html")
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    context = {"message": "Login invalid", "form": AuthenticationForm()}
    return HttpResponse(template.render(context, request))


def logout_form(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

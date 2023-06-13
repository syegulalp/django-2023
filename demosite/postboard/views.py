from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Post


def index(request):
    last_posts = Post.objects.order_by("-date")[:7]
    output = []
    for p in last_posts:
        output.append(f"{p.date}: {p.post_text}")
    return HttpResponse("<p>".join(output))


def template(request):
    last_posts = Post.objects.order_by("-date")[:7]
    template = loader.get_template("index.html")
    context = {"last_posts": last_posts}
    return HttpResponse(template.render(context, request))


def post_new(request):
    new_post_text = request.POST["text_input"]
    new_post = Post(post_text=new_post_text)
    new_post.save()
    return HttpResponseRedirect(reverse("template"))

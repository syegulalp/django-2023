from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    date = models.DateTimeField("posted on", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

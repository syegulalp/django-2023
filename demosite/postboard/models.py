from django.db import models

class Post(models.Model):
    post_text = models.CharField(max_length=200)
    date = models.DateTimeField("posted on", auto_now_add=True)
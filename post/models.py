from django.db import models
from account.models import User
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=30)
    post_content = models.TextField()
    post_thumbnail = models.ImageField(null=True)
    post_key = models.CharField(max_length=50)
    posted_date = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)

class Comment(models.Model):
    comment_message = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commented_date = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)
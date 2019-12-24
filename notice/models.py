from django.db import models
from account.models import User
from post.models import Post

# Create your models here.
class Notice(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    TYPE_CHOICES = (
        ('Newpost', '1'),
        ('Newcomment', '2'),
    )
    post = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    id = models.AutoField(primary_key=True)
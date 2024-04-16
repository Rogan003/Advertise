from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ad(models.Model):
    picture = models.ImageField(upload_to = 'pics')
    username = models.CharField(max_length = 20, unique=True)
    description1 = models.TextField(default = 'Check our page!')
    description2 = models.TextField(default = 'Check our page!')
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    POSTTYPES = (
        ('N', 'normal'),
        ('B', 'bronze'),
        ('S', 'silver'),
        ('G', 'gold'),
    )
    posttype = models.CharField(max_length = 15, choices = POSTTYPES)
    followers = models.IntegerField(default = 0)
    posts = models.IntegerField(default = 0)
    pagetype = models.CharField(max_length = 15)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default = 1)
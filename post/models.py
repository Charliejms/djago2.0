from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post (models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
from sqlite3 import Time
from turtle import update
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    completed = models.BooleanField()
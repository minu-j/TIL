from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    actors = models.ManyToManyField(Actor)
    title = models.CharField(max_length=50)
    overview = models.TextField()
    release_date = models.DateTimeField(auto_now=False)
    poster_path = models.TextField()

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
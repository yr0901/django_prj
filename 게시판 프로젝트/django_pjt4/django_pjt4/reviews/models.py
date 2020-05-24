from django.db import models
from django.conf import settings

# Create your models here.
default_pk = 999

class Movie(models.Model):
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=100)
    released_at = models.DateTimeField()

class Review(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=default_pk)
    movie = models.ForeignKey(Movie, on_delete=models.SET_DEFAULT, default=default_pk)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    review = models.ForeignKey(Review, on_delete=models.SET_DEFAULT, default=default_pk)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=default_pk)





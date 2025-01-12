# Create your models here.

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publish_date = models.DateField()  
    featured_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)

    def __str__(self):
        return self.title

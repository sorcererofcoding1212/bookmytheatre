from django.db import models
from django.urls import reverse

# Create your models here.


class Genre(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Movie(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=500, blank=True)
    certification = models.CharField(max_length=10)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    genres = models.ManyToManyField(to=Genre)
    image = models.URLField(
        default='https://betravingknows.com/wp-content/uploads/2017/06/video-movie-placeholder-image-grey.png')
    runtime = models.PositiveIntegerField(
        help_text='Runtime in minutes', default=120)

    def __str__(self):
        return self.title

    def runtime_display(self):
        return f"{self.runtime // 60}h {self.runtime % 60}m"
    

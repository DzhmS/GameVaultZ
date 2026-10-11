from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    developer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    genres = models.ManyToManyField('Genre', blank=True)
    platforms = models.ManyToManyField('platforms.Platform', blank=True)

    def __str__(self):
        return self.title
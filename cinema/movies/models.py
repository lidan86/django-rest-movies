from django.db import models

# The Genre Model
class Genre(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)

def save(self, *args, **kwargs):
    options = self.name and {'name': self.name} or {}
    super(Genre, self).save(*args, **kwargs)

# The Movie Model
class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

def save(self, *args, **kwargs):
    options = self.title and {'title': self.title} or {}
    super(Movie, self).save(*args, **kwargs)

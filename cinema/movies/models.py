from django.db import models

class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField()
    genre = models.TextField()

    class Meta:
        ordering = ('created',)

def save(self, *args, **kwargs):
    options = self.title and {'title': self.title} or {}
    super(Movie, self).save(*args, **kwargs)

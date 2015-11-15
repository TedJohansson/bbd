from django.db import models

# Create your models here.
class info(models.Model):
    title = models.CharField(max_length=500)
    year = models.CharField(max_length=10)
    rated = models.CharField(max_length=10)
    released = models.CharField(max_length=150)
    runtime = models.CharField(max_length=10)
    genre = models.CharField(max_length=500)
    director = models.CharField(max_length=500)
    writer = models.CharField(max_length=500)
    plot = models.TextField()
    language = models.CharField(max_length=500)
    county = models.CharField(max_length=500)
    awards = models.CharField(max_length=500)
    poster = models.CharField(max_length=500)
    metascore = models.CharField(max_length=5)
    imdbrating = models.CharField(max_length=3)
    imdbvotes = models.CharField(max_length=10)
    imdbid = models.CharField(max_length=25)
    type = models.CharField(max_length=500)
    repsonse = models.CharField(max_length=500)
    actors = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

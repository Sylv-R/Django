from django.db import models
from django.contrib.auth import get_user_model

FilmID = get_user_model()

class Film(models.Model):
    title = models.CharField(max_length=100)
    releaseYear = models.PositiveIntegerField()
    director = models.CharField(max_length=100)
    user = models.ForeignKey(FilmID,on_delete=models.CASCADE)
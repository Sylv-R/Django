from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Film(models.Model):
    title = models.CharField(max_length=100)
    releaseYear = models.PositiveIntegerField()
    director = models.CharField(max_length=100)
    #pk = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.

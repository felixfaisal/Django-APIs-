from django.db import models

# Create your models here.
class Marks(models.Model):
    name = models.CharField(max_length=20)
    marks = models.IntegerField()

class AnimeList(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    description = models.CharField(max_length=100)
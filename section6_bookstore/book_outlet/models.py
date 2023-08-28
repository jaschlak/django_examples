from django.db import models

# Create your models here.

class Book(models.Model):
    # Id created automatically
    title = models.CharField(max_length=50) # From django model fields
    rating = models.IntegerField()
    
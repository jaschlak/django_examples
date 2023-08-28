from django.db import models

# Create your models here.

class Book(models.Model):
    # Id created automatically
    title = models.CharField(max_length=50) # From django model fields
    rating = models.IntegerField()
    
    def __str__(self):
        return "{} ({})".format(self.title, self.rating)
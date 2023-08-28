from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    # Id created automatically
    title = models.CharField(max_length=50) # From django model fields
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100) # allows nulls
    is_bestselling = models.BooleanField(default=False)  # default null values to False
    
    def get_absolute_url(self):
        return reverse("book-detail",args=[self.id])
    
    def __str__(self):
        return "{} ({})".format(self.title, self.rating)
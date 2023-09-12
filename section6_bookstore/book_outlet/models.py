from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Book(models.Model):
    # Id created automatically
    title = models.CharField(max_length=50) # From django model fields
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, null=True) # null values acceptable
    is_bestselling = models.BooleanField(default=False)  # default null values to False
    
    # can use model name in url IE http://localhost:8000/<Book.title value>, fills space with -
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) 
    
    def get_absolute_url(self):
        return reverse("book-detail",args=[self.slug])
    
    def __str__(self):
        return "{} ({})".format(self.title, self.rating)
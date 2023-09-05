from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    # Id created automatically
    title = models.CharField(max_length=50) # From django model fields
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100) # allows nulls
    is_bestselling = models.BooleanField(default=False)  # default null values to False
    
    # can use model name in url IE http://localhost:8000/<Book.title value>, fills space with -
    slug = models.SlugField(default="", editable=False, null=False, db_index=True) 
    
    def get_absolute_url(self):
        return reverse("book-detail",args=[self.slug])
    
    # override built in save method and pass args to built in method
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title) # slug the Book model's title

        super().save( *args, **kwargs)  # make sure djangos method still called
    
    def __str__(self):
        return "{} ({})".format(self.title, self.rating)
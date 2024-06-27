from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='movie/images')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ManyToManyField(
        'self',
        blank=True,
        related_name='sub_categories',
        symmetrical=False
    )

    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text    
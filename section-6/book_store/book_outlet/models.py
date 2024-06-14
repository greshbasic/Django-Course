from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.CharField(max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{'[BEST SELLER!] ' if self.is_bestselling else ''}{self.title} by {self.author} ({self.rating})"
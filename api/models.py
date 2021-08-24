from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    authors = models.CharField(max_length=250, null=True, blank=True)
    published_date = models.CharField(max_length=30 , null=True, blank=True)
    categories = models.CharField(max_length=250, null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    ratings_count = models.PositiveIntegerField(null=True, blank=True)
    thumbnail = models.URLField(max_length=200, null=True, blank=True)

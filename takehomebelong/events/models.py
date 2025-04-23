from django.db import models

# Create your models here.

class Event(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

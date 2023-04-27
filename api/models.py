from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    flight_number = models.CharField(blank=True, max_length=6)
    distance = models.FloatField(default=0)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    type = models.CharField(default='flight')
    notes = models.TextField(blank=True)

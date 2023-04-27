from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    flight_number = models.CharField(max_length=6)
    distance = models.FloatField
    notes = models.TextField(blank=True)

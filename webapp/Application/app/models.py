"""
Definition of models.
"""

#from django.db import models
from djongo import models

# Create your models here.
class User_profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    height=models.DecimalField(max_digits=10, decimal_places=3)
    weight=models.DecimalField(max_digits=10, decimal_places=3)

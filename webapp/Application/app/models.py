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


class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=100)


class symptom(models.Model):
    symptom_id = models.AutoField(primary_key=True)
    symptom_name = models.CharField(max_length=100)


class Symptom_detail(models.Model):
    symptom_id=models.CharField(max_length=10)
    symptom_name=models.CharField(max_length=100)   
    weight  = models.IntegerField() 
    class Meta:
        abstract = True
        

class Disease_symptom(models.Model):
    disease_id = models.CharField(max_length=10)
    disease_name = models.CharField(max_length=100)
    #symptom_details = ListField(EmbeddedModelField('Symptom_detail'))
    symptom_details = models.ArrayField(
        model_container = Symptom_detail,
    )


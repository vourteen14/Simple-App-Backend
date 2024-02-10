from django.db import models

class Animal(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=50)
  breed = models.CharField(max_length=75)
  age = models.IntegerField()
  
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from simple_catalog.utils import random_name

CustomUser = get_user_model()

class Animal(models.Model):
  name = models.CharField(max_length=100)
  species_choices = (
    ('Cat', 'Cat'),
    ('Dog', 'Dog'),
    ('Bird', 'Bird'),
    ('Fish', 'Fish'),
    ('Other', 'Other'),
  )
  species = models.CharField(max_length=50, choices=species_choices)
  breed = models.CharField(max_length=75)
  age = models.FloatField()
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='animals', null=True)
  updated_at = models.DateTimeField(auto_now=True)
  breed_group = models.CharField(max_length=100, blank=True, null=True)
  color_choices = (
    ('black', 'Black'),
    ('white', 'White'),
    ('brown', 'Brown'),
    ('gray', 'Gray'),
    ('orange', 'Orange'),
    ('yellow', 'Yellow'),
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('other', 'Other'),
  )  
  color = models.CharField(max_length=50, choices=color_choices, blank=True, null=True)
  size_choices = (
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
  )
  size = models.CharField(max_length=10, choices=size_choices, blank=True, null=True)
  health_status_choices = (
    ('healthy', 'Healthy'),
    ('sick', 'Sick'),
    ('injured', 'Injured'),
    ('other', 'Other'),
  )
  health_status = models.CharField(max_length=50, choices=health_status_choices, blank=True, null=True)
  adoption_status_choices = (
    ('available', 'Available'),
    ('pending', 'Pending'),
    ('adopted', 'Adopted'),
    ('other', 'Other'),
  )
  adoption_status = models.CharField(max_length=50, choices=adoption_status_choices, blank=True, null=True)
  intake_status_choices = (
    ('stray', 'Stray'),
    ('owner surrender', 'Owner Surrender'),
    ('rescue', 'Rescue'),
    ('other', 'Other'),
  )
  intake_type = models.CharField(max_length=50, blank=True, choices=intake_status_choices, null=True)

  def save(self, *args, **kwargs):
    if not self.pk:
      self.created_at = timezone.now()
    return super().save(*args, **kwargs)

class Image(models.Model):
  image = models.ImageField(upload_to=random_name, blank=True, null=True)
  animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='images', null=True)

  def __str__(self):
    return str(self.animal.id) + '+' + self.animal.name
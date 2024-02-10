from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)
  wa = models.CharField(max_length=15, blank=True)
  photo = models.ImageField(upload_to='photos/', blank=True)

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Animal(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=50)
  breed = models.CharField(max_length=75)
  age = models.FloatField()
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='animals')

  def save(self, *args, **kwargs):
    if not self.pk:
      self.created_at = timezone.now()
    return super().save(*args, **kwargs)

  
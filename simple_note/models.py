from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Note(models.Model):
  name = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notes', null=True)

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    if not self.pk:
      self.created_at = timezone.now()
    return super().save(*args, **kwargs)
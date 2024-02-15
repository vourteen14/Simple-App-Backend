from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Tag(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Todo(models.Model):
  STATUS_CHOICES = [
    ('PL', 'Planned'),
    ('OG', 'Ongoing'),
    ('DN', 'Done'),
    ('HD', 'On Hold'),
    ('CA', 'Canceled'),
  ]
  
  title = models.CharField(max_length=200)
  description = models.TextField()
  status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PL')
  created_at = models.DateTimeField(default=timezone.now, editable=False)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todos', null=True)
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.pk:
      self.created_at = timezone.now()
    return super().save(*args, **kwargs)
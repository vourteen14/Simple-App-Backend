from django.db import models
from django.contrib.auth import get_user_model
from simple_note.utils import random_name

CustomUser = get_user_model()

class Tag(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Contact(models.Model):
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contact')
  name = models.CharField(max_length=100)
  email = models.EmailField()

  def __str__(self):
    return self.name

class Note(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notes')
  tags = models.ManyToManyField(Tag)
  visibility_choices = (
    ('public', 'Public'),
    ('private', 'Private'),
    ('shared', 'Shared'),
  )
  visibility = models.CharField(choices=visibility_choices, default='private', max_length=20)
  priority = models.IntegerField(default=0)
  related_contacts = models.ManyToManyField(Contact)

  def __str__(self):
    return self.title

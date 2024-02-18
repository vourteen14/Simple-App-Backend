from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_user.utils import random_name
from datetime import timedelta
from django.utils import timezone
import os
import uuid

class CustomUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('The Email field must be set')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_active', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')

    return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
  name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  image = models.ImageField(upload_to=random_name, blank=True)
  whatsapp = models.CharField(max_length=15, blank=True)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  activation_token = models.UUIDField(default=uuid.uuid4, editable=False, null=True, unique=True)
  activation_token_created_at = models.DateTimeField(auto_now_add=True, null=True)

  ACTIVATION_TOKEN_EXPIRATION_DAYS = 1

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  class Meta:
    verbose_name = "User"

  def is_activation_token_expired(self):
    if self.activation_token_created_at:
      expiration_date = self.activation_token_created_at + timezone.timedelta(days=self.ACTIVATION_TOKEN_EXPIRATION_DAYS)
      return timezone.now() > expiration_date
    else:
      return False

  def activate(self):
    self.is_active = True
    self.save()

  def generate_activation_link(self):
    return f"http://10.1.0.10:34515/api/auth/activate/{self.activation_token}/"

  def save(self, *args, **kwargs):
    if self.is_active and not self.is_activation_token_expired():
      self.activation_token = None
      self.activation_token_created_at = None
    super().save(*args, **kwargs)

  def __str__(self):
    return self.email

  def has_module_perms(self, app_label):
    return self.is_staff
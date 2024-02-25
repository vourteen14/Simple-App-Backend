import os
import uuid
from django.core.exceptions import ValidationError

def random_name(instance, filename):
  _, ext = os.path.splitext(filename)
  random_name = uuid.uuid4().hex
  return f'notes/{random_name}{ext}'

def priority_validator(data):
  if data not in range(1, 6):
    raise ValidationError("Value must be between 1 and 5")
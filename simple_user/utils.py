import os
import uuid

def random_name(instance, filename):
  _, ext = os.path.splitext(filename)
  random_name = uuid.uuid4().hex
  return f'photos/{random_name}{ext}'
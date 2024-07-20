import os
import uuid
from django.core.mail import send_mail

def send_activation_email(to_email, activation_link):
  mail_subject = 'Activate your account.'
  message = f'Hi,\n\nPlease click on the link below to activate your account:\n\n{activation_link}'
  send_mail(mail_subject, message, 'admin@mail.karuhun.online', [to_email])

def random_name(instance, filename):
  _, ext = os.path.splitext(filename)
  random_name = uuid.uuid4().hex
  return f'photos/{random_name}{ext}'
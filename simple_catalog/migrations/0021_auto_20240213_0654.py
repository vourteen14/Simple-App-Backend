# Generated by Django 4.1.13 on 2024-02-13 06:54

from django.db import migrations
from simple_catalog.models import Animal
from simple_user.models import CustomUser

def forwards_func(apps, schema_editor):
    user = CustomUser.objects.get(email='angga.sr57@gmail.com')

    for animal in Animal.objects.all():
        animal.owner = user
        animal.save()

class Migration(migrations.Migration):

    dependencies = [
        ('simple_catalog', '0020_animal_owner'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
# Generated by Django 4.1.13 on 2024-02-18 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_catalog', '0014_animal_image_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='image_list',
        ),
    ]

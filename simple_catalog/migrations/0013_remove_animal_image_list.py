# Generated by Django 4.1.13 on 2024-02-18 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_catalog', '0012_list_alter_animal_image_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='image_list',
        ),
    ]
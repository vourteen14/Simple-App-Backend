# Generated by Django 4.1.13 on 2024-02-13 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_catalog', '0018_animal_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='test',
        ),
    ]

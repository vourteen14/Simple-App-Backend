# Generated by Django 4.1.13 on 2024-02-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_catalog', '0013_remove_animal_image_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='image_list',
            field=models.ManyToManyField(to='simple_catalog.list'),
        ),
    ]

# Generated by Django 4.1.13 on 2024-02-25 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_catalog', '0022_alter_animal_adoption_status_alter_animal_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='breed_group',
        ),
    ]

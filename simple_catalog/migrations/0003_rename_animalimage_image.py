# Generated by Django 4.1.13 on 2024-02-18 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_catalog', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnimalImage',
            new_name='Image',
        ),
    ]

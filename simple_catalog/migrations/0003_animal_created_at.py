# Generated by Django 4.2.10 on 2024-02-12 11:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simple_catalog', '0002_alter_animal_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]

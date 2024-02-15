# Generated by Django 4.1.13 on 2024-02-13 06:26

from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simple_catalog', '0007_auto_20240213_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
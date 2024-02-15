# Generated by Django 4.1.13 on 2024-02-13 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simple_catalog', '0019_remove_animal_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animals', to=settings.AUTH_USER_MODEL),
        ),
    ]
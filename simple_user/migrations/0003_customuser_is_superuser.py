# Generated by Django 3.2.21 on 2024-02-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_user', '0002_auto_20240210_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
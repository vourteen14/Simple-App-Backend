# Generated by Django 4.1.13 on 2024-02-12 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_user', '0025_customuser_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
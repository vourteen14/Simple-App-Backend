# Generated by Django 4.1.13 on 2024-02-12 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_user', '0016_remove_customuser_wa'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
# Generated by Django 4.1.13 on 2024-02-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_user', '0027_customuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
# Generated by Django 3.2.16 on 2022-12-03 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngaran', '0004_auto_20221203_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ngaran',
            old_name='kota',
            new_name='kotak',
        ),
    ]

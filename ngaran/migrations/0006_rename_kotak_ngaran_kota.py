# Generated by Django 3.2.16 on 2022-12-03 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngaran', '0005_rename_kota_ngaran_kotak'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ngaran',
            old_name='kotak',
            new_name='kota',
        ),
    ]

# Generated by Django 4.1.13 on 2024-02-13 08:36

from django.db import migrations, models
import simple_user.utils
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('simple_user', '0032_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='activation_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, unique=True, upload_to=simple_user.utils.random_name),
        ),
    ]

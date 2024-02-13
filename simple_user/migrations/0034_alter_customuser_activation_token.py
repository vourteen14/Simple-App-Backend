# Generated by Django 4.1.13 on 2024-02-13 08:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('simple_user', '0033_alter_customuser_activation_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='activation_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
    ]

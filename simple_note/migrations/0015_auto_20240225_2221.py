# Generated by Django 4.1.13 on 2024-02-25 15:21

from django.db import migrations
from django.utils import timezone
from simple_note.models import Tag

def fillTag(apps, schema_editor):
    for tag in Tag.objects.all():
        tag.created_at = timezone.now()
        tag.save()

class Migration(migrations.Migration):

    dependencies = [
        ('simple_note', '0014_tag_created_at'),
    ]

    operations = [
        
    ]

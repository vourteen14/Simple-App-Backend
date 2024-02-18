from rest_framework import serializers
from .models import Note
from .models import Tag
from .models import Contact

class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Note
    fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ['pk', 'name']

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = '__all__'
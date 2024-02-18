from rest_framework import serializers
from simple_catalog.models import Animal
from simple_catalog.models import Image

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
  image = ImageSerializer(many=True, source='images', read_only=True)

  class Meta:
    model = Animal
    fields = '__all__'
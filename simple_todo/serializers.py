from rest_framework import serializers
from simple_todo.models import Todo
from simple_todo.models import Tag

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ['tag']
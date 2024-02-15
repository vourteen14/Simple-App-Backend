from django.contrib import admin
from simple_todo.models import Todo
from simple_todo.models import Tag

admin.site.register(Todo)
admin.site.register(Tag)
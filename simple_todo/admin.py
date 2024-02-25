from django.contrib import admin
from simple_todo.models import Todo
from simple_todo.models import Tag

class TagAdmin(admin.ModelAdmin):
  list_display = ('tag', 'id', 'created_at')
  readonly_fields = ['id']

admin.site.register(Todo)
admin.site.register(Tag, TagAdmin)
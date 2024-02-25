from django.contrib import admin
from simple_note.models import Note
from simple_note.models import Tag
from simple_note.models import Contact

class NoteAdmin(admin.ModelAdmin):
  list_display = ('title', 'created_at', 'owner')
  readonly_fields = ('created_at', 'updated_at')

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag)
admin.site.register(Contact)

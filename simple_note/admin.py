from django.contrib import admin
from simple_note.models import Note
from simple_note.models import Attachment
from simple_note.models import Tag
from simple_note.models import Contact

admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Attachment)

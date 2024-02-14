from django.contrib import admin
from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
  search_fields = ['name', 'species', 'breed', 'owner__email']
  list_display = ('name', 'owner')
    
  def owner(self, obj):
    return obj.owner.email if obj.owner else None
    
  owner.short_description = 'Owner'

admin.site.register(Animal, AnimalAdmin)

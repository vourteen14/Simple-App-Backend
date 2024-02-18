from django.contrib import admin
from simple_catalog.models import Animal
from simple_catalog.models import Image

class AnimalAdmin(admin.ModelAdmin):
  search_fields = ['name', 'species', 'breed', 'owner__email']
  list_display = ('name', 'owner', 'health_status', 'adoption_status', 'intake_type')
    
  def owner(self, obj):
    return obj.owner.email if obj.owner else None
    
  owner.short_description = 'Owner'

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Image)

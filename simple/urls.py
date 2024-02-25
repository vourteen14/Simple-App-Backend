from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include('simple_user.urls')),
  path('api/', include('simple_catalog.urls')),
  path('api/', include('simple_note.urls')),
  path('api/', include('simple_todo.urls')),
]
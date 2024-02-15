from django.urls import path
from .views import NoteApiView, TagApiView, ContactApiView

urlpatterns = [
  path('note/', NoteApiView.as_view(), name='note_list'),
  path('note/<int:pk>/', NoteApiView.as_view(), name='note_details'),
  path('note/tag/', TagApiView.as_view(), name='tag_list'),
  path('note/contact/', ContactApiView.as_view(), name='tag_list'),
]
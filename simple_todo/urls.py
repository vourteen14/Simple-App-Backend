from django.urls import path
from simple_todo.views import TodoApiView, TagApiView

urlpatterns = [
  path('todo/', TodoApiView.as_view(), name='todo_list'),
  path('todo/<int:pk>/', TodoApiView.as_view(), name='todo_details'),
  path('todo/tag/', TagApiView.as_view(), name='tag_list'),
]
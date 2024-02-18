from django.urls import path
from simple_catalog.views import AnimalApiView, ImageApiView

urlpatterns = [
  path('animal/', AnimalApiView.as_view(), name='animal_list'),
  path('animal/<int:pk>/', AnimalApiView.as_view(), name='animal_details'),
  path('animal/image/', ImageApiView.as_view(), name='animal_details'),
]
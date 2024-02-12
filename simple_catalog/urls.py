from django.urls import path
from .views import AnimalApiView

urlpatterns = [
  path('animals/', AnimalApiView.as_view(), name='animal_list'),
  path('animals/<int:pk>/', AnimalApiView.as_view(), name='animal_details'),
]
from django.urls import path
from .views import AnimalApiView

urlpatterns = [
  path('animal/', AnimalApiView.as_view(), name='animal_list'),
  path('animal/<int:pk>/', AnimalApiView.as_view(), name='animal_details'),
]
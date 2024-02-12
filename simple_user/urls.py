from django.urls import path
from .views import generate_token, refresh_token

urlpatterns = [
    path('token/', generate_token),
    path('token/refresh/', refresh_token),
]

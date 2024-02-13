from django.urls import path
from .views import generate_token, refresh_token, register_user, activate_user

urlpatterns = [
  path('auth/login/', generate_token),
  path('auth/login/refresh/', refresh_token),
  path('auth/register/', register_user),
  path('auth/activate/<uuid:activation_token>/', activate_user),
]

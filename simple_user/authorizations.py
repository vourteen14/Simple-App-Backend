from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model

def get_user_from_token(token):
  try:
    decoded_token = AccessToken(token)
    user_id = decoded_token['user_id']
    User = get_user_model()
    user = User.objects.get(id=user_id)
    return user.pk
  except Exception as e:
    print(f"Error decoding token: {e}")
    return None
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model

class UserWrapper:
  def __init__(self, user):
    self.data = user

  def __getattr__(self, attr):
    return getattr(self.user, attr)

def get_user_from_token(token):
  try:
    decoded_token = AccessToken(token)
    user_id = decoded_token['user_id']
    User = get_user_model()
    user = User.objects.get(id=user_id)
    return UserWrapper(user)
  except Exception as e:
    print(f"Error decoding token: {e}")
    return None

def get_token_from_request(request):
  authorization_header = request.META.get('HTTP_AUTHORIZATION')
  if authorization_header:
    parts = authorization_header.split()
    if len(parts) == 2:
      return parts[1]
  return None
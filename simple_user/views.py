from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.decorators import api_view

@api_view(['POST'])
def generate_token(request):
  email = request.data.get('email')
  password = request.data.get('password')

  user = authenticate(username=email, password=password)

  if user is not None:
    access_token = AccessToken.for_user(user)
    refresh_token = RefreshToken.for_user(user)
    return JsonResponse({
      'access_token': str(access_token),
      'refresh_token': str(refresh_token)
    }, safe=False)
  else:
    return JsonResponse({'error': 'Invalid credentials'}, safe=False)

@api_view(['POST'])
def refresh_token(request):
  refresh_token = request.data.get('refresh_token')

  if not refresh_token:
    return Response({'error': 'Refresh token is required'}, status=400)

  try:
    refresh_token = RefreshToken(refresh_token)
    access_token = str(refresh_token.access_token)
    return JsonResponse({'access_token': access_token}, safe=False)
  except Exception as e:
    return JsonResponse({'error': str(e)}, safe=False)


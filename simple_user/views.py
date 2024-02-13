from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.decorators import api_view
from .serializers import CustomUserSerializer
from .models import CustomUser

@api_view(['POST'])
def register_user(request):
  if request.method == 'POST':
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      activation_link = user.generate_activation_link()
      serialized_data = serializer.data
      serialized_data['activation_link'] = activation_link
      return JsonResponse(serialized_data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def activate_user(request, activation_token):
  try:
    user = CustomUser.objects.get(activation_token=activation_token)
    if user.is_activation_token_expired():
      return JsonResponse({'result': 'Activation link has expired.'}, status=400)
    else:
      user.activate()
      return JsonResponse({'result': 'Your account has been activated successfully.'}, status=200)
  except CustomUser.DoesNotExist:
    return JsonResponse({'result': 'Invalid activation link.'}, status=404)
  return JsonResponse({'error': 'bad request'}, status=400)

@api_view(['POST'])
def generate_token(request):
  email = request.data.get('email')
  password = request.data.get('password')

  user = authenticate(username=email, password=password)

  if user is not None:
    access_token = AccessToken.for_user(user)
    refresh_token = RefreshToken.for_user(user)
    return JsonResponse({'access_token': str(access_token),'refresh_token': str(refresh_token)}, status=200)
  else:
    return JsonResponse({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
def refresh_token(request):
  refresh_token = request.data.get('refresh_token')

  if not refresh_token:
    return JsonResponse({'error': 'Refresh token is required'}, status=400)

  try:
    refresh_token = RefreshToken(refresh_token)
    access_token = str(refresh_token.access_token)
    return JsonResponse({'access_token': access_token}, status=200)
  except Exception as e:
    return JsonResponse({'error': str(e)}, status=400)


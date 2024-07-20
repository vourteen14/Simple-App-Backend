from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.decorators import api_view
from .utils import send_activation_email
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
      user_email = serialized_data.get('email', None)
      send_activation_email(user_email, activation_link)

      return JsonResponse({'status': 'success', 'code': 201, 'data': serialized_data}, status=201)
    return JsonResponse({'status': 'error', 'code': 400, 'data': serializer.errors}, status=400)

@api_view(['GET'])
def activate_user(request, activation_token):
  try:
    user = CustomUser.objects.get(activation_token=activation_token)
    if user.is_activation_token_expired():
      return JsonResponse({'status': 'error', 'code': 400, 'data': {'result': 'Activation link has expired.'}}, status=400)
    else:
      user.activate()
      return JsonResponse({'status': 'success', 'code': 200, 'data': {'result': 'Your account has been activated successfully.'}}, status=200)
  except CustomUser.DoesNotExist:
    return JsonResponse({'status': 'error', 'code': 404, 'data': {'result': 'Invalid activation link.'}}, status=404)

@api_view(['POST'])
def generate_token(request):
  email = request.data.get('email')
  password = request.data.get('password')

  user = authenticate(username=email, password=password)

  if user is not None:
    access_token = AccessToken.for_user(user)
    refresh_token = RefreshToken.for_user(user)
    return JsonResponse({'status': 'success', 'code': 200, 'data': {'access_token': str(access_token), 'refresh_token': str(refresh_token)}}, status=200)
  else:
    return JsonResponse({'status': 'error', 'code': 400, 'data': {'error': 'Invalid credentials'}}, status=400)

@api_view(['POST'])
def refresh_token(request):
  refresh_token = request.data.get('refresh_token')

  if not refresh_token:
    return JsonResponse({'status': 'error', 'code': 400, 'data': {'error': 'Refresh token is required'}}, status=400)

  try:
    refresh_token = RefreshToken(refresh_token)
    access_token = str(refresh_token.access_token)
    return JsonResponse({'status': 'success', 'code': 200, 'data': {'access_token': access_token}}, status=200)
  except Exception as e:
    return JsonResponse({'status': 'error', 'code': 400, 'data': {'error': str(e)}}, status=400)
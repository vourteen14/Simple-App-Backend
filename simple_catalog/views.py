import json
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from simple_user.authorizations import get_user_from_token
from simple_catalog.models import Animal
from simple_catalog.serializers import AnimalSerializer
from simple_catalog.counters import AnimalCounter

class AnimalApiView(View):
  @csrf_exempt
  def dispatch(self, request, *args, **kwargs):
    try:
      user = JWTAuthentication().authenticate(request)
      if user is None:
        raise AuthenticationFailed('Invalid authentication credentials.')
      return super().dispatch(request, *args, **kwargs)
    except InvalidToken:
      return JsonResponse({'error': 'Invalid token'}, status=401)
    except AuthenticationFailed as e:
      return JsonResponse({'error': str(e)}, status=401)

  def get(self, request, pk=None, *args, **kwargs):
    if pk:
      animal = get_object_or_404(Animal, pk=pk)
      serializer = AnimalSerializer(animal)
      return JsonResponse(serializer.data)
    else:
      animals = Animal.objects.all()
      serializer = AnimalSerializer(animals, many=True)
      return JsonResponse(serializer.data, safe=False)

  def post(self, request, *args, **kwargs):
    try:
      data = json.loads(request.body)
      authorization_header = request.META.get('HTTP_AUTHORIZATION')
      if authorization_header:
        parts = authorization_header.split()
        if len(parts) == 2:
          token = parts[1]
          data['owner'] = get_user_from_token(token)
      serializer = AnimalSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        counter = AnimalCounter()
        counter.increase_animal_count(request.user)
        return JsonResponse(serializer.data, status=201)
      return JsonResponse(serializer.errors, status=400)
    except json.JSONDecodeError:
      return JsonResponse({'error': 'Invalid JSON'}, status=400)

  def put(self, request, pk, *args, **kwargs):
    animal = get_object_or_404(Animal, pk=pk)
    try:
      data = json.loads(request.body)
      serializer = AnimalSerializer(animal, data=data)
      if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
      return JsonResponse(serializer.errors, status=400)
    except json.JSONDecodeError:
      return JsonResponse({'error': 'Invalid JSON'}, status=400)

  def delete(self, request, pk, *args, **kwargs):
    try:
      animal = get_object_or_404(Animal, pk=pk)
      counter = AnimalCounter()
      animal.delete()
      counter.decrease_animal_count(request.user)
      return JsonResponse({}, status=204)
    except IntegrityError:
      return JsonResponse({'error': 'IntegrityError occurred'}, status=500)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=500)
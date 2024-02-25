import json
from django.http import JsonResponse
from django.db import IntegrityError
from django.views import View
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from simple_user.authorizations import get_user_from_token
from simple_user.authorizations import get_token_from_request
from simple_catalog.models import Animal
from simple_catalog.models import Image
from simple_catalog.serializers import AnimalSerializer
from simple_catalog.serializers import ImageSerializer
from simple_catalog.serializers import ImageSerializerAnimal
from simple_catalog.counters import AnimalCounter

class ImageApiView(View):
  @csrf_exempt
  def dispatch(self, request, *args, **kwargs):
    try:
      user = JWTAuthentication().authenticate(request)
      if user is None:
        raise AuthenticationFailed('Invalid authentication credentials.')
      return super().dispatch(request, *args, **kwargs)
    except InvalidToken:
      return JsonResponse({'status': 'error', 'code': 401, 'data': {'error': 'Invalid token'}}, status=401)
    except AuthenticationFailed as e:
      return JsonResponse({'status': 'error', 'code': 401, 'data': {'error': str(e)}}, status=401)

  def post(self, request, *args, **kwargs):
    try:
      serializer = ImageSerializer(data=request.POST.copy())
      user = get_user_from_token(get_token_from_request(request))
      serializer.initial_data['owner'] = user.data.pk
      if serializer.is_valid():
        serializer.save()
        return JsonResponse({'status': 'success', 'code': 201, 'data': [serializer.data]}, status=201)
      return JsonResponse({'status': 'error', 'code': 400, 'data': serializer.errors}, status=400)
    except json.JSONDecodeError:
      return JsonResponse({'status': 'error', 'code': 400, 'data': {'error': 'Invalid JSON'}}, status=400)

class AnimalApiView(View):
  @csrf_exempt
  def dispatch(self, request, *args, **kwargs):
    try:
      user = JWTAuthentication().authenticate(request)
      if user is None:
        raise AuthenticationFailed('Invalid authentication credentials.')
      return super().dispatch(request, *args, **kwargs)
    except InvalidToken:
      return JsonResponse({'status': 'error', 'code': 401, 'data': {'error': 'Invalid token'}}, status=401)
    except AuthenticationFailed as e:
      return JsonResponse({'status': 'error', 'code': 401, 'data': {'error': str(e)}}, status=401)

  def get(self, request, pk=None, *args, **kwargs):
    if pk:
      try:
        animal = Animal.objects.get(pk=pk)
        serializer = AnimalSerializer(animal)
        return JsonResponse({'status': 'success', 'code': 200, 'data': [serializer.data]})
      except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'code': 404, 'data': {'error': 'Animal not found'}}, status=404)
    else:
      user = get_user_from_token(get_token_from_request(request))
      animals = Animal.objects.filter(owner=user.data.pk)
      serializer = AnimalSerializer(animals, many=True)
      return JsonResponse({'status': 'success', 'code': 200, 'data': serializer.data}, status=200)

  def post(self, request, *args, **kwargs):
    try:
      serializer = AnimalSerializer(data=json.loads(request.body))
      user = get_user_from_token(get_token_from_request(request))
      serializer.initial_data['owner'] = user.data.pk
      if serializer.is_valid():
        serializer.save()
        animal_instance = Animal.objects.get(id=serializer.data.get('id'))
        for img_id in serializer.initial_data.get('images'):
          img = Image.objects.get(id=img_id)
          img_data = ImageSerializerAnimal(data=img)
          img_serializer = ImageSerializerAnimal(data={'id': img_id, 'animal': animal_instance.id})
          if img_serializer.is_valid():
            img_serializer.update(img, img_serializer.validated_data)
          else:
            print(img_serializer.errors)
        counter = AnimalCounter()
        counter.increase_animal_count(user.data.pk)
        return JsonResponse({'status': 'success', 'code': 201, 'data': serializer.data}, status=201)
      return JsonResponse({'status': 'error', 'code': 400, 'data': serializer.errors}, status=400)
    except json.JSONDecodeError:
      return JsonResponse({'status': 'error', 'code': 400, 'data': {'error': 'Invalid JSON'}}, status=400)

  def put(self, request, pk, *args, **kwargs):
    if pk:
      animal = get_object_or_404(Animal, pk=pk)
      try:
        data = json.loads(request.body)
        serializer = AnimalSerializer(animal, data=data)
        if serializer.is_valid():
          serializer.save()
          return JsonResponse({'status': 'success', 'code': 200, 'data': [serializer.data]})
        return JsonResponse({'status': 'error', 'code': 400, 'data': serializer.errors}, status=400)
      except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'code': 400, 'data': {'error': 'Invalid JSON'}}, status=400)
    return JsonResponse({'status': 'error', 'code': 404, 'data': {'error': 'Animal not found'}}, status=404)

  def delete(self, request, pk, *args, **kwargs):
    if pk:
      try:
        animal = Animal.objects.get(pk=pk)
        user = get_user_from_token(get_token_from_request(request))
        counter = AnimalCounter()
        animal.delete()
        counter.decrease_animal_count(user.data.pk)
        return JsonResponse({'status': 'success', 'code': 204, 'data': {}}, status=204)
      except IntegrityError:
        return JsonResponse({'status': 'error', 'code': 500, 'data': {'error': 'IntegrityError occurred'}}, status=500)
      except Exception as e:
        return JsonResponse({'status': 'error', 'code': 500, 'data': {'error': str(e)}}, status=500)
    return JsonResponse({'status': 'error', 'code': 404, 'data': {'error': 'Animal not found'}}, status=404)
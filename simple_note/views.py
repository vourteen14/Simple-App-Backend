import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from django.db import IntegrityError
from simple_note.models import Note
from simple_note.models import Tag
from simple_note.models import Contact
from simple_note.serializers import NoteSerializer
from simple_note.serializers import TagSerializer
from simple_note.serializers import ContactSerializer
from simple_user.authorizations import get_user_from_token
from simple_user.authorizations import get_token_from_request

class NoteApiView(View):
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
        note = Note.objects.get(pk=pk)
        serializer = NoteSerializer(note)
        return JsonResponse({'status': 'success', 'code': 200, 'data': [serializer.data]})
      except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'code': 404, 'data': {'error': 'Note not found'}}, status=404)
    else:
      user = get_user_from_token(get_token_from_request(request))
      notes = Note.objects.filter(owner=user.data.pk)
      serializer = NoteSerializer(notes, many=True)
      return JsonResponse({'status': 'success', 'code': 200, 'data': serializer.data}, safe=False)

  def post(self, request, *args, **kwargs):
    try:
      token = None
      data = json.loads(request.body)
      user = get_user_from_token(get_token_from_request(request))
      data['owner'] = user.data.pk
      serializer = NoteSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        return JsonResponse({'status': 'success', 'code': 201, 'data': [serializer.data]}, status=201)
      return JsonResponse({'status': 'error', 'code': 400, 'data': serializer.errors}, status=400)
    except json.JSONDecodeError:
      return JsonResponse({'status': 'error', 'code': 400, 'data': {'error': 'Invalid JSON'}}, status=400)

  def put(self, request, pk, *args, **kwargs):
    if pk:
      animal = get_object_or_404(Note, pk=pk)
      try:
        data = json.loads(request.body)
        user = get_user_from_token(get_token_from_request(request))
        data['owner'] = user.data.pk
        serializer = NoteSerializer(animal, data=data)
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
        notes = Note.objects.get(pk=pk)
        notes.delete()
        return JsonResponse({'status': 'success', 'code': 204, 'data': {}}, status=204)
      except IntegrityError:
        return JsonResponse({'status': 'error', 'code': 500, 'data': {'error': 'IntegrityError occurred'}}, status=500)
      except Exception as e:
        return JsonResponse({'status': 'error', 'code': 500, 'data': {'error': str(e)}}, status=500)
    return JsonResponse({'status': 'error', 'code': 404, 'data': {'error': 'Animal not found'}}, status=404)

class TagApiView(View):
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

  def get(self, request, *args, **kwargs):
    tag = Tag.objects.all()
    serializer = TagSerializer(tag, many=True)
    return JsonResponse({'status': 'success', 'code': 200, 'data': serializer.data}, safe=False)

  def post(self, request, *args, **kwargs):
    try:
      token = None
      data = json.loads(request.body)
      user = get_user_from_token(get_token_from_request(request))
      data['owner'] = user.data.pk
      serializer = TagSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        return JsonResponse({'status': 'success', 'code': 201, 'data': [serializer.data]}, status=201)
      return JsonResponse({'status': 'error', 'code': 400, 'data': serializer.errors}, status=400)
    except json.JSONDecodeError:
      return JsonResponse({'status': 'error', 'code': 400, 'data': {'error': 'Invalid JSON'}}, status=400)

class ContactApiView(View):
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

  def get(self, request, *args, **kwargs):
    user = get_user_from_token(get_token_from_request(request))
    contact = Contact.objects.filter(owner=user.data.pk)
    serializer = ContactSerializer(contact, many=True)
    return JsonResponse({'status': 'success', 'code': 200, 'data': serializer.data}, safe=False)

  def post(self, request, *args, **kwargs):
    try:
      token = None
      data = json.loads(request.body)
      user = get_user_from_token(get_token_from_request(request))
      data['owner'] = user.data.pk
      serializer = ContactSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        return JsonResponse({'status': 'success', 'code': 201, 'data': [serializer.data]}, status=201)
      return JsonResponse({'status': 'error', 'code': 400, 'data': serializer.errors}, status=400)
    except json.JSONDecodeError:
      return JsonResponse({'status': 'error', 'code': 400, 'data': {'error': 'Invalid JSON'}}, status=400)

  def delete(self, request, pk, *args, **kwargs):
    if pk:
      try:
        contacts = Contact.objects.get(pk=pk)
        contacts.delete()
        return JsonResponse({'status': 'success', 'code': 204, 'data': {}}, status=204)
      except IntegrityError:
        return JsonResponse({'status': 'error', 'code': 500, 'data': {'error': 'IntegrityError occurred'}}, status=500)
      except Exception as e:
        return JsonResponse({'status': 'error', 'code': 500, 'data': {'error': str(e)}}, status=500)
    return JsonResponse({'status': 'error', 'code': 404, 'data': {'error': 'Animal not found'}}, status=404)
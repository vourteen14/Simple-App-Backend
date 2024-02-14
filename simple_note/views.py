import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from simple_note.models import Note
from simple_note.serializers import NoteSerializer
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
      serializer = NotesSerializer(notes, many=True)
      return JsonResponse({'status': 'success', 'code': 200, 'data': serializer.data}, safe=False)

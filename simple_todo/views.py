from django.shortcuts import render

class TodoApiView(View):
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
      return JsonResponse({'status': 'success', 'code': 200, 'data': serializer.data}, safe=False)

  def post(self, request, *args, **kwargs):
    try:
      token = None
      data = json.loads(request.body)
      user = get_user_from_token(get_token_from_request(request))
      data['owner'] = user.data.pk
      serializer = AnimalSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        counter = AnimalCounter()
        counter.increase_animal_count(user.data.pk)
        return JsonResponse({'status': 'success', 'code': 201, 'data': [serializer.data]}, status=201)
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
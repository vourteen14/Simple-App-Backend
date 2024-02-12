from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Animal
from .serializers import AnimalSerializer

class AnimalApiView(View):
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
    serializer = AnimalSerializer(data=request.POST)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

  def put(self, request, pk, *args, **kwargs):
    animal = get_object_or_404(Animal, pk=pk)
    serializer = AnimalSerializer(animal, data=request.POST)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  def delete(self, request, pk, *args, **kwargs):
    animal = get_object_or_404(Animal, pk=pk)
    animal.delete()
    return JsonResponse({}, status=204)

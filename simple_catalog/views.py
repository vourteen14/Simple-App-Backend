from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permission
from .models import Animal
from .serializers import AnimalSerializer

class AnimalApiView(APIView)
  permission_classes = [permission.IsAuthenticated]

  def get(self, request, pk, *args, **kwargs):
    return Response()
  
  def post(self, request, *args, **kwargs):
    return Response()

  def put(self, request, *args, **kwargs):
    return Response()

  def delete(self, request, pk, *args, **kwargs):
    return Response()


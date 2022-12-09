from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NgaranSerializer
from .models import Ngaran

class NgaranViews(APIView):
  def post(self, request):
    serializer = NgaranSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"response": "ok", "result": serializer.data}, status=status.HTTP_200_OK)
    else:
      return Response({"response": "fail", "result": serializer.fails}, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
    if id:
      try:
        item = Ngaran.objects.get(id=id)
        serializer = NgaranSerializer(item)
        return Response({"response": "ok", "result": serializer.data}, status=status.HTTP_200_OK)
      except Ngaran.DoesNotExist:
        return Response({"response": "fail", "result": "No data found"}, status=status.HTTP_404_NOT_FOUND)

    if Ngaran.objects.all():
      items = Ngaran.objects.all()
      serializer = NgaranSerializer(items, many=True)
      return Response({"response": "ok", "result": serializer.data}, status=status.HTTP_200_OK)
    else:
      return Response({"response": "fail", "result": "No result found"}, status=status.HTTP_404_NOT_FOUND)

  def patch(self, request, id=None):
    item = Ngaran.objects.get(id=id)
    serializer = NgaranSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({"response": "ok", "result": serializer.data})
    else:
      return Response({"response": "fail", "result": serializer.fails})

  def put(self, request, id=None):
    item = Ngaran.objects.get(id=id)
    serializer = NgaranSerializer(item, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"response": "ok", "result": serializer.data})
    else:
      return Response({"response": "fail", "result": serializer.fails})

  def delete(self, request, id=None):
    try:
      item = Ngaran.objects.get(id=id)
      item.delete()
      return Response({"response": "ok", "result": "Data with ID " + str(id) + " has been deleted"})
    except:
      return Response({"response": "fail", "result": "Data with ID " + str(id) + " not found" })

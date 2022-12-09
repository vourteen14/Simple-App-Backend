from rest_framework import serializers
from .models import Ngaran

class NgaranSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ngaran
    fields = ('__all__')

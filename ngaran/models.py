from django.db import models

class Ngaran(models.Model):
  nama = models.CharField(max_length=60, blank=False, default='')
  kota = models.CharField(max_length=50, blank=False, default='')
  pekerjaan = models.CharField(max_length=100, blank=False, default='')


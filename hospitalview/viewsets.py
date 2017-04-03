from .models import Zona, Habitacion, Cama, Estado, CamaEstado, TipoCama
from serializers import ZonaSerializer, HabitacionSerializer, CamaSerializer, EstadoSerializer, CamaEstadoSerializer, TipoCamaSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics

class ZonaViewSet(viewsets.ModelViewSet):
     serializer_class = ZonaSerializer
     queryset = Zona.objects.all()

class HabitacionViewSet(viewsets.ModelViewSet):
     serializer_class = HabitacionSerializer
     queryset = Habitacion.objects.all()

class CamaViewSet(viewsets.ModelViewSet):
     serializer_class = CamaSerializer
     queryset = Cama.objects.all()

class EstadoViewSet(viewsets.ModelViewSet):
     serializer_class = EstadoSerializer
     queryset = Estado.objects.all()

class CamaEstadoViewSet(viewsets.ModelViewSet):
     serializer_class = CamaEstadoSerializer
     queryset = CamaEstado.objects.all()

class TipoCamaViewSet(viewsets.ModelViewSet):
     serializer_class = TipoCamaSerializer
     queryset = TipoCama.objects.all()


     #filter_fields = ('usuario','fecha')
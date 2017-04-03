from rest_framework import serializers
from models import Zona, Habitacion, Cama, Estado, CamaEstado, TipoCama

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = ('id', 'nombre', 'descripcion', 'numero_piso')

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ('id', 'nombre')

class CamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cama
        fields = ('id', 'nombre', 'descripcion', 'activo', 'reservado', 'id_zona', 'id_estado')        

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('id', 'nombre', 'descripcion', 'color')

class CamaEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamaEstado
        fields = ('id', 'fecha', 'hora', 'tiempo', 'id_cama', 'id_estad')

class TipoCamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCama
        fields = ('id', 'nombre', 'descripcion')
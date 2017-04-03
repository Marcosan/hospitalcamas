from django.db import models

import datetime

# Create your models here.
class Zona(models.Model):
    nombre =  models.TextField(max_length=50)
    descripcion =  models.TextField(max_length=50)
    numero_piso =  models.IntegerField();
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"

class Habitacion(models.Model):
    nombre =  models.TextField(max_length=50)
    #id_zona = models.ForeignKey(Zona, related_name='zona')
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

class Estado(models.Model):
    nombre =  models.TextField(max_length=50)
    descripcion =  models.TextField(max_length=50)
    color =  models.TextField(max_length=50)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

class Cama(models.Model):
    nombre =  models.TextField(max_length=50)
    descripcion =  models.TextField(max_length=50)
    activo = models.BooleanField(default=True)
    reservado = models.BooleanField(default=False)
    id_zona = models.ForeignKey(Zona, related_name='zona')
    id_estado = models.ForeignKey(Estado, related_name='estado')
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cama"
        verbose_name_plural = "Camas"


class CamaEstado(models.Model):
    fecha = models.TextField(max_length=12)
    hora = models.TextField(max_length=12)
    tiempo = models.TextField(max_length=12)
    id_cama = models.ForeignKey(Cama, related_name='cama')
    id_estad = models.ForeignKey(Estado, related_name='estad')

    class Meta:
        verbose_name = "Cama_Estado"
        verbose_name_plural = "Cama_Estados"

class TipoCama(models.Model):
    nombre =  models.TextField(max_length=50)
    descripcion =  models.TextField(max_length=50)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "TipoCama"
        verbose_name_plural = "TiposCama"
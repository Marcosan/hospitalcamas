from django.contrib import admin
from django.db import models
from models import *

import datetime

# Create your models here.

class User(models.Model):
    nombre =  models.TextField(max_length=15)
    apellido =  models.TextField(max_length=15)
    cedula =  models.TextField(max_length=11)
    correo =  models.TextField(max_length=25)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

admin.site.register(Zona)
admin.site.register(Habitacion)
admin.site.register(Cama)
admin.site.register(Estado)
admin.site.register(CamaEstado)
admin.site.register(TipoCama)

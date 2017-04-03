from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import JsonResponse
import json
import time
from django.core import serializers
#por revisar
from django.views.decorators.csrf import csrf_exempt
#from push_notifications.models import GCMDevice,APNSDevice

from rest_framework import viewsets

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden

#from push_notifications.models import GCMDevice

from .models import Zona, Habitacion, Cama, Estado, CamaEstado, TipoCama

# Create your views here.

def CamasView(request):
	#zona = Zona.objects.get(pk=request.GET['valorpk']) #?valorpk=1
	zona_actual = Zona.objects.get(id=request.GET['zona'])  #valores repetidos en la fk
	cama_actual = Cama.objects.filter(id_zona=zona_actual.id)
	#cama_actual = Cama.objects.filter(pk=hab_actual.id)
	#cama_estado = CamaEstado.objects.filter(id_cama=cama)
	#cama_estado = CamaEstado.objects.prefetch_related('cama')
    #inspecciones = Cama.objects.filter(cama=cama)
	context = {
    	'zonas':  Zona.objects.all().order_by('-id'),
    	'habitaciones':  Habitacion.objects.all().order_by('-id'),
    	'camas':  Cama.objects.all().order_by('-id'),
    	'estados':  Estado.objects.all().order_by('-id'),
    	'tiposcama':  TipoCama.objects.all().order_by('-id'),
    	'cama_estado': CamaEstado.objects.all().order_by('-id'),
    	'zona_actual': zona_actual,
    	#'hab_actual': hab_actual,
    	'cama_actual': cama_actual
    }
	
	return render(request, 'camasview.html', context)

def CamasEdit(request):
    #zona = Zona.objects.get(pk=request.GET['valorpk']) #?valorpk=1
    zona_actual = Zona.objects.get(id=request.GET['zona'])  #valores repetidos en la fk
    cama_actual = Cama.objects.filter(id_zona=zona_actual.id)
    #cama_actual = Cama.objects.filter(pk=hab_actual.id)
    #cama_estado = CamaEstado.objects.filter(id_cama=cama)
    #cama_estado = CamaEstado.objects.prefetch_related('cama')
    #inspecciones = Cama.objects.filter(cama=cama)
    context = {
        'zonas':  Zona.objects.all().order_by('-id'),
        'habitaciones':  Habitacion.objects.all().order_by('-id'),
        'camas':  Cama.objects.all().order_by('-id'),
        'estados':  Estado.objects.all().order_by('-id'),
        'tiposcama':  TipoCama.objects.all().order_by('-id'),
        'cama_estado': CamaEstado.objects.all().order_by('-id'),
        'zona_actual': zona_actual,
        #'hab_actual': hab_actual,
        'cama_actual': cama_actual
    }
    
    return render(request, 'camasedit.html', context)

def ZonasView(request):
    
    context = {
        'zonas':  Zona.objects.all().order_by('-id'),
        'habitaciones':  Habitacion.objects.all().order_by('-id'),
        'camas':  Cama.objects.all().order_by('-id'),
        'estados':  Estado.objects.all().order_by('-id'),
        'tiposcama':  TipoCama.objects.all().order_by('-id'),
        'cama_estado': CamaEstado.objects.all().order_by('-id'),
    }
    
    return render(request, 'zonas.html', context)

def PanelView(request):
    anio = "16"
    dia_ini = 2
    dia_fin = 18
    est_ocupado = Estado.objects.filter(nombre="OCUPADO")
    est_egreso = Estado.objects.filter(nombre="EGRESO")
    est_desocupado = Estado.objects.filter(nombre="DESOCUPADO")
    est_limp_desinf = Estado.objects.filter(nombre="LIMPIEZA Y DESINFECCION")
    est_habilitada = Estado.objects.filter(nombre="HABILITADA")

    ce_ocupado = CamaEstado.objects.filter(id_estad=est_ocupado)
    ce_egreso = CamaEstado.objects.filter(id_estad=est_egreso)
    ce_desocupado = CamaEstado.objects.filter(id_estad=est_desocupado)
    ce_limp_desinf = CamaEstado.objects.filter(id_estad=est_limp_desinf)
    ce_habilitada = CamaEstado.objects.filter(id_estad=est_habilitada)

    resp_oc = {}
    resp_eg = {}
    resp_des = {}
    resp_l_d = {}
    resp_hab = {}
    #for c in ce_ocupado:
        #resp_oc["Enero"] = 

    context = {
        'cama_estado': CamaEstado.objects.all().order_by('-id'),
        #resp_oc
    }
    
    return render(request, 'panel.html', context)

def getIndicadoresPorDia(request):
    #if request.method == 'GET':
    r = {}
    response = []
    estado = "OCUPADO"
    dia_ini = "01"
    dia_fin = "07"
    mes_ini = "06"
    mes_fin = "06"
    anio = "16"
    zona_actual = Zona.objects.get(id=request.GET['zona'])
    camas = Cama.objects.filter(id_zona=zona_actual.id).select_related()
    estados = Estado.objects.all();

    for c in camas:
        resp = {}
        resp["id"] = c.id
        resp["nombre"] = c.nombre
        resp["descripcion"] = c.descripcion
        resp["activo"] = c.activo
        resp["reservado"] = c.reservado
        resp["zona"] = c.id_zona.nombre
        resp["estado"] = c.id_estado.nombre
        response.append(resp)
    #for a in response:
    #    print a
        
    return JsonResponse(response, safe=False)

def getCamasEstado(zona):
    camas_return = []
    
    camas = Cama.objects.filter(id_zona=zona)
    estados = Estado.objects.all();
    cama_estado = CamaEstado.objects.filter(id_estado=estados, id_cama=camas)
    
    for c_e in cama_estado:
        camas_return.append(c_e)
    
    return camas_return

def getCamasEstadoJson(request):
    #if request.method == 'GET':
    r = {}
    response = []
    
    zona_actual = Zona.objects.get(id=request.GET['zona'])
    camas = Cama.objects.filter(id_zona=zona_actual.id).select_related()
    estados = Estado.objects.all();

    for c in camas:
        resp = {}
        resp["id"] = c.id
        resp["nombre"] = c.nombre
        resp["descripcion"] = c.descripcion
        resp["activo"] = c.activo
        resp["reservado"] = c.reservado
        resp["zona"] = c.id_zona.nombre
        resp["estado"] = c.id_estado.nombre
        response.append(resp)
    #for a in response:
    #    print a
        
    return JsonResponse(response, safe=False)

def getZonasEstadoJson(request):
    #if request.method == 'GET':
    r = {}
    response = []
    zonas_cont = {}
    cont = 0
    camas = Cama.objects.all()
    estados = Estado.objects.all()
    zonas = Zona.objects.all()

    for z in zonas:
        zonas_cont[z.nombre] = 0

    for c in camas:
        resp = {}
        resp["id"] = c.id
        resp["nombre"] = c.nombre
        resp["descripcion"] = c.descripcion
        resp["activo"] = c.activo
        resp["reservado"] = c.reservado
        resp["zona"] = c.id_zona.nombre
        resp["estado"] = c.id_estado.nombre
        if c.id_estado.nombre == "EGRESO":
            zonas_cont[c.id_zona.nombre] = zonas_cont[c.id_zona.nombre] + 1
        response.append(resp)
    #for a in response:
    #    if a.estado == "EGRESO":
    #        zonas_cont[a.zona] = cont + 1
    cont = 0

    context = {
        'zonas_cont': zonas_cont,
    }

    return JsonResponse(context, safe=False)

def getContEstadosJson(request):
    #if request.method == 'GET':
    r = {}
    response = []
    estados_cont = {}
    cont = 0
    camas = Cama.objects.all()
    estados = Estado.objects.all()
    zonas = Zona.objects.all()

    for e in estados:
        estados_cont[e.nombre] = 0

    for c in camas:
        resp = {}
        resp["id"] = c.id
        resp["nombre"] = c.nombre
        resp["descripcion"] = c.descripcion
        resp["activo"] = c.activo
        resp["reservado"] = c.reservado
        resp["zona"] = c.id_zona.nombre
        resp["estado"] = c.id_estado.nombre
        
        estados_cont[c.id_estado.nombre] = estados_cont[c.id_estado.nombre] + 1
        response.append(resp)
    
    cont = 0

    context = {
        'estados_cont': estados_cont,
    }

    return JsonResponse(context, safe=False)
    

def postEstadosCama(request):
    if(request.method == 'GET'):

        id_cama = request.GET.get('id_cama', None)
        est = request.GET.get('est', None)
        if id_cama is None or est is None:
            return HttpResponseBadRequest()
        
        estado = Estado.objects.filter(nombre__icontains=est)
        
        if list(estado):

            cama = Cama.objects.get(id=id_cama)
            cama.id_estado = estado[0]
            cama.save()
        else:
            return HttpResponse(status=500)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def postReservado(request):
    if(request.method == 'GET'):

        id_cama = request.GET.get('id_cama', None)
        reservadoGet = request.GET.get('res', None)
        if id_cama is None or reservadoGet is None:
            return HttpResponseBadRequest()
        cama = Cama.objects.get(id=id_cama)
        
        if reservadoGet == "true":
            cama.reservado = True
        else:
            cama.reservado = False
        cama.save()
        
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

def postInhabilitado(request):
    if(request.method == 'GET'):

        id_cama = request.GET.get('id_cama', None)
        inhGet = request.GET.get('inh', None)
        if id_cama is None or inhGet is None:
            return HttpResponseBadRequest()
        cama = Cama.objects.get(id=id_cama)
        
        if inhGet == "true":
            cama.activo = True
        else:
            cama.activo = False
        cama.save()
        
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

def postCamaEstado(request):
    if(request.method == 'GET'):

        id_cama = request.GET.get('id_cama', None)
        est = request.GET.get('est', None)
        tiempo = request.GET.get('tiempo', None)
        
        if id_cama is None or est is None or tiempo is None:
            return HttpResponseBadRequest()
        
        
        estado = Estado.objects.filter(nombre__icontains=est)
        cama = Cama.objects.filter(id__icontains=id_cama)
        cama_estado = CamaEstado.objects.all();
        hora = time.strftime("%H:%M:%S")
        fecha = time.strftime("%d/%m/%y")
        #cama_estado.fecha_inicio = time
        
        b = CamaEstado.objects.create(fecha=fecha, hora=hora, tiempo=tiempo, id_cama = cama[0], id_estad = estado[0])
        b.save()
        #cama_estado.save()
        print "hola"
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)
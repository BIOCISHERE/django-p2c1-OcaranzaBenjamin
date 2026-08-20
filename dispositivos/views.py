from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse(
        "<h1>EcoEnergy</h1>"
        "<p>Back End en funcionamiento</p>"
    )

# dispositivos/views.py
def dispositivos_zona(request, zona_id):
    if zona_id != 3:
        return HttpResponse(
            "Zona no encontrada", status=404
        )
    return HttpResponse(
        f"Dispositivos de la zona {zona_id}"
    )

def zona_id(request, zona_id):
    if zona_id == 0:
        return HttpResponse(
            "Zona no encontrada o valida", status=404
        )
    return HttpResponse(
        f"Zona con ID: {zona_id}"
    )
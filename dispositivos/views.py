from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(
        request,
        "dispositivos/inicio.html",
        contexto,
    )

# dispositivos/views.py
def dispositivos_zona(request):
    zonas = [
        {"nombre": "Zona norte grande", "superficie": "185148"},
        {"nombre": "Zona central", "superficie": "143913"},
        {"nombre": "Zona sur", "superficie": "233243"},
    ]
    return render(
        request,
        "dispositivos/zonas.html",
        {"zonas": zonas},
    )

def zona_id(request, zona_id):
    if zona_id == 0:
        return HttpResponse(
            "Zona no encontrada o valida", status=404
        )
    return HttpResponse(
        f"Zona con ID: {zona_id}"
    )

def catalogo(request):
    dispositivos = [
        {"nombre": "Medidor inteligente", "estado": "Activo"},
        {"nombre": "Sensor de temperatura", "estado": "Activo"},
        {"nombre": "Climatizador", "estado": "Revisión"},
    ]
    return render(
        request,
        "dispositivos/catalogo.html",
        {"dispositivos": dispositivos},
    )
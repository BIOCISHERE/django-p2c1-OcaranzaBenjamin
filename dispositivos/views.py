from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .services import cargar_dispositivos, cargar_zonas

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
    zonas = cargar_zonas()
    activos = sum(
        1 for item in zonas
        if item["estado"] == "Activo"
    )
    contexto = {
        "zonas": zonas,
        "total": len(zonas),
        "total_activos": activos
    }
    return render(
        request, "dispositivos/zonas.html", contexto
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
    dispositivos = cargar_dispositivos()
    activos = sum(
        1 for item in dispositivos
        if item["estado"] == "Activo"
    )
    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        "total_activos": activos,
    }
    return render(
        request, "dispositivos/catalogo.html", contexto
    )
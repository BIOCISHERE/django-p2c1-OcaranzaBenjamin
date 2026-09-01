from django.http import Http404
from django.shortcuts import render

from .services import cargar_categorias, cargar_dispositivos, cargar_zonas


def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
        "autor": "Benjamin Ocaranza Costa"
    }
    return render(
        request,
        "dispositivos/inicio.html",
        contexto,
    )


def _estado_zona(consumo_total, limite_kwh):
    return "ALERTA" if consumo_total > limite_kwh else "NORMAL"


def dispositivos_zona(request):
    zonas = cargar_zonas()
    dispositivos = cargar_dispositivos()

    zonas_con_detalle = []
    for zona in zonas:
        zona_dispositivos = [
            dispositivo for dispositivo in dispositivos
            if dispositivo["zona_id"] == zona["id"]
        ]
        consumo_total = sum(
            dispositivo["consumo_kwh"] for dispositivo in zona_dispositivos
        )
        zonas_con_detalle.append(
            {
                "id": zona["id"],
                "nombre": zona["nombre"],
                "limite_kwh": zona["limite_kwh"],
                "cantidad_dispositivos": len(zona_dispositivos),
                "consumo_total": consumo_total,
                "estado": _estado_zona(consumo_total, zona["limite_kwh"]),
            }
        )

    contexto = {
        "zonas": zonas_con_detalle,
        "total": len(zonas_con_detalle),
        "total_alertas": sum(
            1 for zona in zonas_con_detalle if zona["estado"] == "ALERTA"
        ),
        "total_normales": sum(
            1 for zona in zonas_con_detalle if zona["estado"] == "NORMAL"
        ),
    }
    return render(request, "dispositivos/zonas.html", contexto)


def zona_id(request, zona_id):
    zonas = cargar_zonas()
    zona = next((item for item in zonas if item["id"] == zona_id), None)
    if zona is None:
        raise Http404("Zona no encontrada")

    dispositivos = cargar_dispositivos()
    dispositivos_zona = [
        {
            **dispositivo,
            "categoria": next(
                (
                    categoria["nombre"]
                    for categoria in cargar_categorias()
                    if categoria["id"] == dispositivo["categoria_id"]
                ),
                "Sin categoría",
            ),
        }
        for dispositivo in dispositivos
        if dispositivo["zona_id"] == zona_id
    ]
    consumo_total = sum(dispositivo["consumo_kwh"] for dispositivo in dispositivos_zona)
    estado = "ALERTA" if consumo_total > zona["limite_kwh"] else "NORMAL"

    return render(
        request,
        "dispositivos/detalles.html",
        {
            "zona_actual": zona,
            "dispositivos": dispositivos_zona,
            "consumo_total": consumo_total,
            "total": len(dispositivos_zona),
            "estado": estado,
            "total_activos": sum(1 for item in dispositivos if item["consumo_kwh"] > 0),
        },
    )


def catalogo(request):
    dispositivos = cargar_dispositivos()
    categorias = cargar_categorias()
    categoria_por_id = {categoria["id"]: categoria["nombre"] for categoria in categorias}

    activos = sum(1 for item in dispositivos if item["consumo_kwh"] > 0)
    contexto = {
        "dispositivos": [
            {
                **dispositivo,
                "categoria": categoria_por_id.get(dispositivo["categoria_id"], "Sin categoría"),
            }
            for dispositivo in dispositivos
        ],
        "total": len(dispositivos),
        "total_activos": activos,
    }
    return render(request, "dispositivos/dispositivos.html", contexto)

import json
from django.conf import settings


def cargar_dispositivos():
    ruta = settings.BASE_DIR / "data" / 'dispositivos.json'
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de dispositivos")
    return datos


def cargar_categorias():
    ruta = settings.BASE_DIR / "data" / 'categorias.json'
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de categorías")
    return datos


def cargar_zonas():
    ruta = settings.BASE_DIR / "data" / 'zonas.json'
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de zonas")
    return datos
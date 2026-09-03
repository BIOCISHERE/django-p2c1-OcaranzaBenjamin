from django.urls import path
from . import views
app_name = "dispositivos"
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("zonas/<int:zona_id>/", views.zona_id, name="por_id"),
    path("dispositivos/", views.catalogo, name="catalogo"),
    path("resumen-zonas/", views.dispositivos_zona, name="zonas")
]
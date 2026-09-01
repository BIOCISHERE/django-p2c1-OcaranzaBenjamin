# EcoEnergy

Aplicación web desarrollada en Python con Django para el monitoreo energético de zonas y dispositivos. El proyecto consume datos desde archivos JSON y presenta una interfaz responsive con Bootstrap 5 para visualizar el estado de consumo por zona y el catálogo completo de dispositivos.

## Descripción

EcoEnergy es una solución en etapa de prototipo orientada a la gestión de consumo energético por áreas o zonas. La aplicación muestra:

- una pantalla de inicio
- un listado de zonas con su estado, límite de consumo y consumo total
- el detalle de una zona determinada con sus dispositivos asociados
- un catálogo general de dispositivos

La lógica de negocio se implementa en `dispositivos/views.py`, la carga de datos se centraliza en `dispositivos/services.py` y la presentación se realiza con plantillas Django en `templates/`.

## Estado actual del proyecto

La aplicación ya está funcionando con estas funcionalidades:

- navegación principal desde `base.html`
- vista de inicio (`/`)
- listado de zonas (`/zonas/`)
- detalle de zona por id (`/zonas/<int:zona_id>/`)
- catálogo de dispositivos (`/dispositivos/`)
- cálculo de estado por zona (`NORMAL` o `ALERTA`)
- integración con Bootstrap 5 para diseño responsive
- carga de datos desde JSON en `data/`
- pruebas automatizadas para las vistas principales

No hay persistencia en base de datos ni modelos de Django para dominio aún; la información se lee desde archivos JSON.

## Tecnologías

- Python 3.13
- Django 6.1
- SQLite
- Bootstrap 5 a través de `django-bootstrap5`
- HTML + Django Templates
- JSON como fuente de datos de prueba

## Requisitos previos

- Python instalado
- Git
- acceso a la terminal del proyecto

Se recomienda verificar la versión con:

```bash
python --version
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/BIOCISHERE/django-p2c1-OcaranzaBenjamin.git
cd django-p2c1-OcaranzaBenjamin
```

Crear y activar entorno virtual:

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configuración

El proyecto usa Django con configuración base estándar. La clave secreta y otros valores de entorno pueden definirse según la configuración local del entorno.

Ejemplo para macOS/Linux:

```bash
export DJANGO_SECRET_KEY="una-clave-secreta"
```

Ejemplo para Windows PowerShell:

```powershell
$env:DJANGO_SECRET_KEY = "una-clave-secreta"
```

Si no se define una clave, Django puede usar una predeterminada para desarrollo local, pero es recomendable configurar una clave segura en entornos reales.

## Datos JSON

Los archivos de prueba se encuentran en la carpeta `data/`:

- `data/zonas.json`
- `data/dispositivos.json`
- `data/categorias.json`

Ejemplo de estructura de zonas:

```json
[
    {
        "id": 1,
        "nombre": "Bodega Norte",
        "limite_kwh": 500
    }
]
```

Ejemplo de estructura de dispositivos:

```json
[
    {
        "id": 1,
        "nombre": "Aire Acondicionado A1",
        "consumo_kwh": 150,
        "zona_id": 1,
        "categoria_id": 1
    }
]
```

La carga de datos está centralizada en `dispositivos/services.py` con funciones como:

- `cargar_zonas()`
- `cargar_dispositivos()`
- `cargar_categorias()`

Cada una abre el archivo JSON correspondiente y valida que el contenido sea una lista.

## Estructura principal del proyecto

```text
config/
    settings.py
    urls.py
    asgi.py
    wsgi.py

dispositivos/
    admin.py
    apps.py
    models.py
    services.py
    tests.py
    urls.py
    views.py
    migrations/

data/
    categorias.json
    dispositivos.json
    zonas.json

templates/
    base.html
    dispositivos/
        inicio.html
        zonas.html
        detalles.html
        dispositivos.html

manage.py
requirements.txt
README.md
```

## Rutas disponibles

Las rutas de la aplicación se registran en `dispositivos/urls.py`:

| Método | Ruta                | Descripción                              |
| ------ | ------------------- | ---------------------------------------- |
| GET    | `/`                 | Página de inicio                         |
| GET    | `/zonas/`           | Listado de zonas                         |
| GET    | `/zonas/<zona_id>/` | Detalle de una zona con sus dispositivos |
| GET    | `/dispositivos/`    | Catálogo general de dispositivos         |
| GET    | `/admin/`           | Panel administrativo de Django           |

Ejemplos de uso:

```bash
python manage.py runserver
```

Luego abrir:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/zonas/
- http://127.0.0.1:8000/zonas/2/
- http://127.0.0.1:8000/dispositivos/

## Funcionalidad actual

### Inicio

La vista de inicio presenta una landing page con una propuesta visual de EcoEnergy y enlaces rápidos a zonas y dispositivos.

### Zonas

`/zonas/` calcula por cada zona:

- cantidad de dispositivos
- consumo total
- límite de consumo
- estado: `NORMAL` o `ALERTA`

La vista utiliza la plantilla `templates/dispositivos/zonas.html`.

### Detalle de zona

`/zonas/<zona_id>/` muestra:

- nombre de la zona
- límite de consumo
- consumo total
- número de dispositivos
- estado
- listado de dispositivos asociados

La navegación tiene un botón para volver al listado de zonas.

### Dispositivos

`/dispositivos/` lista todos los dispositivos con su categoría y su consumo en kWh.

## Diseño responsive

La base visual del proyecto usa Bootstrap 5 en `templates/base.html`. Las plantillas están diseñadas con:

- contenedores responsivos
- filas y columnas con `row` y `col-*`
- cards para métricas y contenido
- tablas con `table-responsive`
- botones adaptados para móvil y escritorio

Esto permite que la interfaz se adapte a distintos tamaños de pantalla sin romper la experiencia.

## Pruebas

El proyecto cuenta con pruebas para las vistas principales en `dispositivos/tests.py`.

Ejecutarlas:

```bash
python manage.py test
```

Resultado verificado en el proyecto actual:

```text
Ran 3 tests in 0.005s

OK
```

## Dependencias

En `requirements.txt` se declara:

```text
asgiref==3.12.1
Django==6.1
django-bootstrap5==26.2
sqlparse==0.6.0
```

## Estado y próximos pasos

El proyecto ya alcanzó el estado funcional solicitado para el caso actual: listas dinámicas desde JSON, detalle de zona por dispositivo y visualización responsive. Como continuación natural, los próximos pasos posibles son:

- migrar la fuente de datos a modelos de Django
- persistir zonas y dispositivos en base de datos
- agregar formularios y validaciones
- implementar autenticación y permisos
- preparar la aplicación para entorno de producción

## Comandos útiles

Validar el proyecto:

```bash
python manage.py check
```

Ejecutar servidor:

```bash
python manage.py runserver
```

Crear superusuario:

```bash
python manage.py createsuperuser
```

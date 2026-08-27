# EcoEnergy

Aplicacion web inicial desarrollada con Python y Django para el proyecto
integrado **EcoEnergy**. Actualmente presenta informacion de monitoreo
energetico mediante paginas HTML de demostracion.

## Descripcion

El proyecto contiene un proyecto Django llamado `config` y una aplicacion
llamada `dispositivos`. La interfaz usa una plantilla base con navegacion hacia
las vistas de inicio, dispositivos y zonas.

Los datos de dispositivos y zonas se almacenan en archivos JSON y se cargan
desde `dispositivos/services.py`. En el estado actual no existen modelos de
negocio, consultas a la base de datos ni operaciones CRUD.

## Tecnologias

- Python compatible con Django 6.1.
- Django 6.1.
- SQLite para la base de datos local.
- Plantillas HTML de Django.
- `django-bootstrap5` para cargar Bootstrap 5 desde las plantillas.
- ASGI y WSGI para los puntos de entrada del proyecto.

## Requisitos previos

- Python instalado y disponible desde la terminal.
- Git instalado.
- Una terminal ubicada en la carpeta del proyecto.

Se recomienda comprobar la version de Python con `python --version` o
`python3 --version`. El proyecto fue ejecutado en desarrollo con Python 3.13.

## Instalacion

Clona el repositorio y entra en su carpeta:

```bash
git clone https://github.com/BIOCISHERE/django-p2c1-OcaranzaBenjamin.git
cd django-p2c1-OcaranzaBenjamin
```

Crea y activa un entorno virtual.

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Instala las dependencias fijadas:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configuracion

La clave secreta se obtiene desde `DJANGO_SECRET_KEY`. El archivo
`.env.example` muestra el nombre de la variable esperada:

En macOS o Linux:

```bash
export DJANGO_SECRET_KEY="una-clave-secreta-unica"
```

En Windows PowerShell:

```powershell
$env:DJANGO_SECRET_KEY = "una-clave-secreta-unica"
```

El proyecto no carga automaticamente archivos `.env`. Si no se define la
variable, se utiliza una clave predeterminada para desarrollo local.

La configuracion actual mantiene `DEBUG = True`, `ALLOWED_HOSTS` vacio y una
base de datos SQLite en `db.sqlite3`. Estos valores deben revisarse antes de un
despliegue en produccion.

## Datos JSON y carga

Los datos de zonas se encuentran en `data/zonas.json`. El archivo contiene una
lista de objetos con esta estructura:

```json
{
	"id": 1,
	"nombre": "Oficina Central",
	"tipo": "Interior",
	"limite_consumo_kwh": 150.0,
	"estado": "Activo"
}
```

La funcion `cargar_zonas()` de `dispositivos/services.py` construye la ruta
`settings.BASE_DIR / "data" / "zonas.json"`, abre el archivo con codificacion
UTF-8 y comprueba que el contenido sea una lista. La vista
`dispositivos_zona()` usa esa funcion y envia los datos al template
`dispositivos/zonas.html` mediante la variable `zonas`.

Los dispositivos se cargan de forma equivalente desde
`data/dispositivos.json` mediante `cargar_dispositivos()`.

## Base de datos

Ejecuta las migraciones de las aplicaciones incluidas en Django cuando prepares
el entorno local:

```bash
python manage.py migrate
```

La aplicacion `dispositivos` no tiene modelos ni migraciones propias en este
momento. Los listados de zonas y dispositivos que se muestran en pantalla son
datos de prueba definidos directamente en `dispositivos/views.py`.

## Ejecucion

Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre <http://127.0.0.1:8000/> en el navegador.

## Vistas y rutas disponibles

Las rutas de `dispositivos` se incluyen desde la raiz del proyecto.

| Metodo | Ruta                | Resultado                                                  |
| ------ | ------------------- | ---------------------------------------------------------- |
| GET    | `/`                 | Pagina de inicio de EcoEnergy.                             |
| GET    | `/dispositivos/`    | Catalogo de dispositivos cargados desde JSON.              |
| GET    | `/zonas/`           | Listado de zonas cargadas desde JSON.                       |
| GET    | `/zonas/<zona_id>/` | Muestra el ID de la zona. El ID `0` responde con HTTP 404. |
| GET    | `/admin/`           | Panel administrativo de Django; requiere un superusuario.  |

Ejemplos:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/dispositivos/
curl http://127.0.0.1:8000/zonas/
curl http://127.0.0.1:8000/zonas/3/
```

## Dependencia externa

El paquete externo `django-bootstrap5==26.2` se declara en `requirements.txt`.
Es necesario porque `base.html` carga la biblioteca `django_bootstrap5` y usa
las etiquetas `{% bootstrap_css %}` y `{% bootstrap_javascript %}` para
incorporar Bootstrap 5 en las paginas heredadas.

La evidencia de esta dependencia se encuentra en estos archivos:

- `requirements.txt`: version fijada de `django-bootstrap5`.
- `config/settings.py`: aplicacion `django_bootstrap5` instalada.
- `templates/base.html`: carga CSS y JavaScript de Bootstrap.

## Justificacion y prueba

Los archivos JSON permiten mantener los datos de demostracion fuera del codigo
de las vistas y reutilizar una funcion de carga para cada conjunto de datos.
Esto se comprueba en `dispositivos/services.py`, donde `cargar_zonas()` y
`cargar_dispositivos()` leen sus respectivos archivos, y en `dispositivos/views.py`,
donde las vistas llaman a esas funciones antes de renderizar sus templates.

La ruta funcional de zonas es `/zonas/`, declarada en `dispositivos/urls.py`
con el nombre `zonas` y conectada con `dispositivos_zona`.

## Verificacion

Comprueba la instalacion y la configuracion del proyecto:

```bash
python manage.py check
```

Ejecuta la suite disponible:

```bash
python manage.py test
```

Actualmente el chequeo de Django finaliza sin errores. El comando de pruebas no
encuentra casos implementados en `dispositivos/tests.py`.

Para crear un usuario administrador local:

```bash
python manage.py createsuperuser
```

## Estructura principal

```text
config/                 Configuracion, URLs y entradas ASGI/WSGI
dispositivos/           Aplicacion principal
	migrations/           Migraciones de la aplicacion
	admin.py              Registro del panel administrativo
	apps.py               Configuracion de la aplicacion
	models.py             Modelos de datos, actualmente vacio
	urls.py               Rutas de la aplicacion
	views.py              Vistas y preparacion del contexto
	services.py           Carga de datos desde archivos JSON
templates/              Plantillas HTML compartidas
	base.html             Plantilla base y navegacion
	dispositivos/         Plantillas de inicio, catalogo y zonas
manage.py               Utilidad de administracion de Django
requirements.txt        Dependencias fijadas
db.sqlite3              Base de datos local ignorada por Git
```

## Estado actual y pendientes

La interfaz basica ya esta disponible, pero el proyecto aun se encuentra en
fase de prototipo:

- Los datos de zonas y dispositivos se leen desde archivos JSON y no se
	persisten en modelos de la base de datos.
- No hay modelos, formularios, autenticacion propia ni permisos de negocio.
- No hay endpoints CRUD ni API REST.
- No hay pruebas automatizadas del dominio.
- La configuracion de seguridad y despliegue requiere ajustes para produccion.

## Proximos pasos

- Definir los requerimientos funcionales del caso EcoEnergy.
- Diseñar modelos para zonas, dispositivos, estados y mediciones.
- Reemplazar los datos estaticos por persistencia en la base de datos.
- Corregir y ampliar las plantillas y la navegacion.
- Implementar validaciones, formularios y permisos.
- Agregar pruebas unitarias y de integracion para vistas y modelos.
- Revisar `DEBUG`, `ALLOWED_HOSTS`, `SECRET_KEY` y el servidor de produccion.

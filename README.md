# EcoEnergy

Aplicacion web inicial desarrollada con Python y Django para el proyecto
integrado **EcoEnergy**. Actualmente presenta informacion de monitoreo
energetico mediante paginas HTML de demostracion.

## Descripcion

El proyecto contiene un proyecto Django llamado `config` y una aplicacion
llamada `dispositivos`. La interfaz usa una plantilla base con navegacion hacia
las vistas de inicio, dispositivos y zonas.

Los datos mostrados por las vistas son estaticos y se definen en memoria. En el
estado actual no existen modelos de negocio, consultas a la base de datos ni
operaciones CRUD.

## Tecnologias

- Python compatible con Django 6.1.
- Django 6.1.
- SQLite para la base de datos local.
- Plantillas HTML de Django.
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
| GET    | `/dispositivos/`    | Catalogo estatico con tres dispositivos y su estado.       |
| GET    | `/zonas/`           | Listado estatico con tres zonas y su superficie.           |
| GET    | `/zonas/<zona_id>/` | Muestra el ID de la zona. El ID `0` responde con HTTP 404. |
| GET    | `/admin/`           | Panel administrativo de Django; requiere un superusuario.  |

Ejemplos:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/dispositivos/
curl http://127.0.0.1:8000/zonas/
curl http://127.0.0.1:8000/zonas/3/
```

## Verificacion

Comprueba la instalacion y la configuracion del proyecto:

```bash
python manage.py check
```

Ejecuta la suite disponible:

```bash
python manage.py test
```

Actualmente el chequeo de Django finaliza sin errores, pero no hay casos de
prueba implementados en `dispositivos/tests.py`.

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
	views.py              Vistas y datos estaticos de demostracion
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

- Los datos de zonas y dispositivos no se persisten.
- No hay modelos, formularios, autenticacion propia ni permisos de negocio.
- No hay endpoints CRUD ni API REST.
- No hay pruebas automatizadas del dominio.
- La plantilla de zonas debe corregirse para mostrar la superficie de cada zona;
  actualmente referencia una variable de dispositivo que no existe en ese
  contexto.
- La configuracion de seguridad y despliegue requiere ajustes para produccion.

## Proximos pasos

- Definir los requerimientos funcionales del caso EcoEnergy.
- Diseñar modelos para zonas, dispositivos, estados y mediciones.
- Reemplazar los datos estaticos por persistencia en la base de datos.
- Corregir y ampliar las plantillas y la navegacion.
- Implementar validaciones, formularios y permisos.
- Agregar pruebas unitarias y de integracion para vistas y modelos.
- Revisar `DEBUG`, `ALLOWED_HOSTS`, `SECRET_KEY` y el servidor de produccion.

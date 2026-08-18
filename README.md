# EcoEnergy

Backend inicial desarrollado con Python y Django para el proyecto integrado cuyo caso se denomina **EcoEnergy**.

## Descripcion y objetivo

Actualmente, este repositorio contiene un esqueleto base de Django. Su objetivo es servir como punto de partida para comenzar el desarrollo del proyecto integrado cuando se entregue la definicion del caso y sus funcionalidades.

## Requisitos previos

- Python instalado y disponible desde la terminal.
- Git instalado.
- Una terminal ubicada en la carpeta donde se clonara el proyecto.

La version de Python requerida por el proyecto aun no esta definida. Se recomienda utilizar una version de Python compatible con la version de Django indicada en `requirements.txt` y comprobarla con `python --version`.

## Clonacion del repositorio

```bash
git clone https://github.com/BIOCISHERE/django-p2c1-OcaranzaBenjamin.git
cd django-p2c1-OcaranzaBenjamin
```

## Creacion y activacion del entorno virtual

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

## Instalacion de dependencias

Con el entorno virtual activado:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Comandos de verificacion

Comprobar las versiones disponibles:

```bash
python --version
python -m pip --version
```

Comprobar la configuracion del proyecto Django:

```bash
python manage.py check
```

## Estado actual

El proyecto se encuentra en una etapa inicial y actualmente funciona como una estructura base para Django. Todavia no se han definido ni implementado las funcionalidades del caso EcoEnergy.

## Proximos pasos

- Recibir la definicion del caso EcoEnergy.
- Identificar los requerimientos y funcionalidades del proyecto.
- Diseñar e implementar las aplicaciones, modelos, vistas y endpoints necesarios.
- Agregar pruebas y actualizar esta documentacion conforme avance el desarrollo.

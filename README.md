# Platos

Aplicación web en Django para mostrar una carta de platos con búsqueda, detalle, propina y etiquetas del tipo de plato.

## Requisitos

- Python 3.12
- Virtualenv
- Git

## 1) Clonar el proyecto

```bash
git clone https://github.com/benjamorales3102/platos.git
cd platos
```

## 2) Crear entorno virtual

```bash
python -m venv .venv
```

### En Windows

```bash
.venv\Scripts\Activate.ps1
```

### En macOS/Linux

```bash
source .venv/bin/activate
```

## 3) Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4) Ejecutar migraciones

```bash
python manage.py migrate
```

## 5) Iniciar el servidor

```bash
python manage.py runserver
```

Luego abre en el navegador:

```text
http://127.0.0.1:8000/
```

## 6) Acceder a la aplicación

- Portada: http://127.0.0.1:8000/
- Detalle de un plato: http://127.0.0.1:8000/1/

## Estructura principal

- `config/` — configuración del proyecto
- `platos/` — app principal con vistas, templates, datos y estilos
- `manage.py` — script principal de Django

## Nota

Si aparece la advertencia de migraciones pendientes, ejecuta:

```bash
python manage.py migrate
```

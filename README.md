# Aplicativo - Control e Informes

Herramienta web para **cargar y previsualizar informes en Excel**. Permite subir un archivo `.xlsx`/`.xls` y visualizar las primeras 5 filas con su encabezado para validar el contenido antes de procesarlo.

## Stack
- Python 3.14 + Flask (patrón MVC)
- Gestionado con [uv](https://github.com/astral-sh/uv)
- pandas + openpyxl para leer Excel
- Docker para despliegue

## Ejecutar localmente
```bash
uv sync
uv run flask --app app:create_app run --port 8000
```
Abrir http://127.0.0.1:8000

## Ejecutar con Docker
```bash
docker build -t excel-preview .
docker run --rm -p 8000:8000 excel-preview
```

## Estructura
```
app.py                 # Entry (factory Flask)
models/                # Lógica de negocio (lectura Excel)
controllers/           # Rutas (Blueprint)
views/templates/       # Plantillas Jinja
uploads/               # Archivos subidos (ignorados por git)
```

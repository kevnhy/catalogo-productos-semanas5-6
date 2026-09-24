# Catálogo de Productos — Semanas 5 y 6

**Estudiante:** Kevin Robles  
**Lenguaje:** Python 3  
**Interfaz gráfica:** Flet

Proyecto académico que integra las colecciones y operaciones CRUD de la Semana 5 con una interfaz gráfica y manejo de eventos de la Semana 6.

## 1. Funcionalidades

- Agregar productos.
- Buscar productos por código.
- Listar productos registrados.
- Actualizar nombre y precio.
- Eliminar productos.
- Validar campos obligatorios y precios.
- Evitar códigos duplicados.
- Mostrar mensajes de éxito y error.
- Cargar tres productos de ejemplo al iniciar.

## 2. Colecciones utilizadas

El proyecto utiliza las tres colecciones solicitadas para Python:

- **`list` (`productos`)**: mantiene los productos en orden y permite construir el listado de la interfaz.
- **`dict` (`indice`)**: relaciona cada código con su objeto `Producto` y facilita la búsqueda.
- **`set` (`codigos`)**: mantiene los códigos únicos y permite detectar duplicados.

La clase `Catalogo` mantiene las tres estructuras sincronizadas al agregar y eliminar productos.

## 3. Programación orientada a objetos

- `Producto` es la clase base.
- `ProductoFisico` hereda de `Producto`.
- `ProductoDigital` hereda de `Producto`.
- Se utilizan propiedades para validar código, nombre y precio.

## 4. Interfaz y eventos

La interfaz está desarrollada con Flet. Los botones tienen eventos asociados:

- **Agregar** → crea un objeto y lo registra en el catálogo.
- **Buscar** → consulta el diccionario por código y muestra los datos.
- **Actualizar** → modifica nombre y precio del producto encontrado.
- **Eliminar** → elimina el producto de `list`, `dict` y `set`.
- **Limpiar** → vacía los campos del formulario.

## 5. Estructura del proyecto

```text
Semanas5y6/
├── main.py
├── requirements.txt
├── README.md
├── diagramas/
│   └── UML.txt
├── docs/
│   └── capturas/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── catalogo.py
│   ├── producto.py
│   ├── producto_digital.py
│   └── producto_fisico.py
└── tests/
    └── test_catalogo.py
```

## 6. Requisitos

- Python 3.10 o superior.
- Flet.
- Conexión a Internet únicamente para instalar la dependencia si no está disponible localmente.

## 7. Instalación y ejecución

Desde la carpeta raíz del proyecto:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## 8. Ejecutar las pruebas

Desde la raíz del proyecto:

```bash
python -m unittest discover -s tests -v
```

Las pruebas comprueban agregar/buscar, actualizar, eliminar, duplicados y validación de precios.

## 9. GitHub

Antes de entregar, publicar este proyecto en un repositorio público de GitHub y reemplazar el enlace de abajo por la URL real:

**Repositorio:** `PEGAR_AQUI_LA_URL_PUBLICA_DE_GITHUB`

## 10. Datos de prueba

Al iniciar la aplicación se cargan:

| Código | Producto | Precio | Tipo |
|---|---|---:|---|
| P001 | Mouse Gamer | $25.00 | Producto base |
| P002 | Teclado Mecánico | $45.00 | Físico |
| P003 | Curso de Python | $30.00 | Digital |


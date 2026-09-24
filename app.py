import flet as ft

from .catalogo import Catalogo
from .producto import Producto


APP_TITLE = "Catálogo de Productos | Semanas 5 y 6"


def main(page: ft.Page):
    page.title = APP_TITLE
    page.padding = 24
    page.bgcolor = ft.Colors.GREY_50
    page.window_width = 980
    page.window_height = 760
    page.window_min_width = 720
    page.window_min_height = 620

    catalogo = Catalogo()
    catalogo.cargar_datos_prueba()

    codigo = ft.TextField(label="Código", hint_text="Ej. P004", expand=True)
    nombre = ft.TextField(label="Nombre", hint_text="Nombre del producto", expand=True)
    precio = ft.TextField(label="Precio", hint_text="Ej. 29.99", expand=True)

    mensaje = ft.Text(size=14)
    lista = ft.Column(spacing=8, scroll=ft.ScrollMode.AUTO, expand=True)
    contador = ft.Text(size=13, color=ft.Colors.GREY_700)

    def mostrar_mensaje(texto: str, correcto: bool = True):
        mensaje.value = texto
        mensaje.color = ft.Colors.GREEN_700 if correcto else ft.Colors.RED_700
        page.update()

    def refrescar():
        productos = catalogo.listar()
        lista.controls = [
            ft.Container(
                content=ft.Row(
                    [
                        ft.Text(producto.codigo, weight=ft.FontWeight.BOLD, width=90),
                        ft.Text(producto.nombre, expand=True),
                        ft.Text(f"${producto.precio:.2f}", width=100, text_align=ft.TextAlign.RIGHT),
                    ]
                ),
                padding=12,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.GREY_200),
                border_radius=8,
            )
            for producto in productos
        ]
        contador.value = f"{len(productos)} producto(s) registrado(s)"
        page.update()

    def limpiar(_=None):
        codigo.value = ""
        nombre.value = ""
        precio.value = ""
        page.update()

    def validar_campos() -> tuple[str, str, float]:
        cod = codigo.value.strip()
        nom = nombre.value.strip()
        if not cod or not nom or not precio.value.strip():
            raise ValueError("Completa código, nombre y precio.")
        try:
            pre = float(precio.value.replace(",", "."))
        except ValueError as exc:
            raise ValueError("El precio debe ser un número válido.") from exc
        if pre < 0:
            raise ValueError("El precio no puede ser negativo.")
        return cod, nom, pre

    def agregar(_):
        try:
            cod, nom, pre = validar_campos()
            catalogo.agregar(Producto(cod, nom, pre))
            limpiar()
            refrescar()
            mostrar_mensaje("✓ Producto agregado correctamente.")
        except ValueError as exc:
            mostrar_mensaje(f"✕ {exc}", False)

    def buscar(_):
        cod = codigo.value.strip()
        if not cod:
            mostrar_mensaje("✕ Ingresa un código para buscar.", False)
            return
        producto = catalogo.buscar(cod)
        if producto:
            nombre.value = producto.nombre
            precio.value = f"{producto.precio:.2f}"
            mostrar_mensaje("✓ Producto encontrado.")
        else:
            mostrar_mensaje("✕ Producto no encontrado.", False)

    def actualizar(_):
        try:
            cod, nom, pre = validar_campos()
            catalogo.actualizar(cod, nom, pre)
            refrescar()
            mostrar_mensaje("✓ Producto actualizado correctamente.")
        except ValueError as exc:
            mostrar_mensaje(f"✕ {exc}", False)

    def eliminar(_):
        cod = codigo.value.strip()
        if not cod:
            mostrar_mensaje("✕ Ingresa un código para eliminar.", False)
            return
        try:
            catalogo.eliminar(cod)
            limpiar()
            refrescar()
            mostrar_mensaje("✓ Producto eliminado correctamente.")
        except ValueError as exc:
            mostrar_mensaje(f"✕ {exc}", False)

    encabezado = ft.Container(
        content=ft.Column(
            [
                ft.Text("Catálogo de Productos", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Semanas 5 y 6 · Colecciones, CRUD, Flet y manejo de eventos", color=ft.Colors.GREY_700),
            ],
            spacing=4,
        ),
        padding=ft.padding.only(bottom=14),
    )

    formulario = ft.Container(
        content=ft.Column(
            [
                ft.Text("Datos del producto", size=18, weight=ft.FontWeight.BOLD),
                ft.Row([codigo, nombre, precio], spacing=12),
                ft.Row(
                    [
                        ft.ElevatedButton("Agregar", icon=ft.Icons.ADD, on_click=agregar),
                        ft.ElevatedButton("Buscar", icon=ft.Icons.SEARCH, on_click=buscar),
                        ft.ElevatedButton("Actualizar", icon=ft.Icons.EDIT, on_click=actualizar),
                        ft.ElevatedButton("Eliminar", icon=ft.Icons.DELETE, on_click=eliminar),
                        ft.OutlinedButton("Limpiar", icon=ft.Icons.CLEAR, on_click=limpiar),
                    ],
                    wrap=True,
                    spacing=8,
                ),
                mensaje,
            ],
            spacing=12,
        ),
        padding=18,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_200),
        border_radius=12,
    )

    listado = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Text("Productos registrados", size=19, weight=ft.FontWeight.BOLD), contador],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Text("Código", weight=ft.FontWeight.BOLD, width=90),
                            ft.Text("Nombre", weight=ft.FontWeight.BOLD, expand=True),
                            ft.Text("Precio", weight=ft.FontWeight.BOLD, width=100, text_align=ft.TextAlign.RIGHT),
                        ]
                    ),
                    padding=ft.padding.symmetric(horizontal=12, vertical=8),
                ),
                lista,
            ],
            expand=True,
        ),
        padding=18,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_200),
        border_radius=12,
        expand=True,
    )

    page.add(encabezado, formulario, ft.Container(height=12), listado)
    refrescar()

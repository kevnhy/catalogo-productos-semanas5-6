from typing import Optional

from .producto import Producto
from .producto_digital import ProductoDigital
from .producto_fisico import ProductoFisico


class Catalogo:
    """Administra productos usando list, dict y set."""

    def __init__(self) -> None:
        # list: conserva el orden para listar los productos.
        self.productos: list[Producto] = []
        # dict: permite localizar un producto por código de forma directa.
        self.indice: dict[str, Producto] = {}
        # set: evita que existan códigos repetidos.
        self.codigos: set[str] = set()

    def agregar(self, producto: Producto) -> None:
        codigo = producto.codigo
        if codigo in self.codigos:
            raise ValueError("Ya existe un producto con ese código.")
        self.productos.append(producto)
        self.indice[codigo] = producto
        self.codigos.add(codigo)

    def buscar(self, codigo: str) -> Optional[Producto]:
        return self.indice.get(str(codigo).strip())

    def listar(self) -> list[Producto]:
        return list(self.productos)

    def actualizar(self, codigo: str, nombre: str, precio: float) -> None:
        producto = self.buscar(codigo)
        if producto is None:
            raise ValueError("Producto no encontrado.")
        producto.nombre = nombre
        producto.precio = precio

    def eliminar(self, codigo: str) -> None:
        codigo = str(codigo).strip()
        producto = self.buscar(codigo)
        if producto is None:
            raise ValueError("Producto no encontrado.")
        self.productos.remove(producto)
        self.indice.pop(codigo, None)
        self.codigos.discard(codigo)

    def cargar_datos_prueba(self) -> None:
        """Carga ejemplos para demostrar la aplicación al iniciarla."""
        ejemplos = [
            Producto("P001", "Mouse Gamer", 25.00),
            ProductoFisico("P002", "Teclado Mecánico", 45.00, 0.80),
            ProductoDigital("P003", "Curso de Python", 30.00, "MP4"),
        ]
        for producto in ejemplos:
            self.agregar(producto)

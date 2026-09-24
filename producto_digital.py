from .producto import Producto


class ProductoDigital(Producto):
    """Producto que representa contenido digital."""

    def __init__(self, codigo: str, nombre: str, precio: float, formato: str):
        super().__init__(codigo, nombre, precio)
        self.formato = str(formato).strip()

    def __str__(self) -> str:
        return f"{super().__str__()} - Digital - {self.formato}"

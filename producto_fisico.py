from .producto import Producto


class ProductoFisico(Producto):
    """Producto que representa un artículo físico."""

    def __init__(self, codigo: str, nombre: str, precio: float, peso: float):
        super().__init__(codigo, nombre, precio)
        self.peso = float(peso)

    def __str__(self) -> str:
        return f"{super().__str__()} - Físico - {self.peso:.2f} kg"

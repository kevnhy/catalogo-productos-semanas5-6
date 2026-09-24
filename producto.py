class Producto:
    """Representa un producto básico del catálogo."""

    def __init__(self, codigo: str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        valor = str(valor).strip()
        if not valor:
            raise ValueError("El código es obligatorio.")
        self._codigo = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        valor = str(valor).strip()
        if not valor:
            raise ValueError("El nombre es obligatorio.")
        self._nombre = valor

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        try:
            valor = float(valor)
        except (TypeError, ValueError) as exc:
            raise ValueError("El precio debe ser numérico.") from exc
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} - ${self.precio:.2f}"

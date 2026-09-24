import unittest

from src.catalogo import Catalogo
from src.producto import Producto


class TestCatalogo(unittest.TestCase):
    def setUp(self):
        self.catalogo = Catalogo()

    def test_agregar_y_buscar(self):
        producto = Producto("P1", "Mouse", 25)
        self.catalogo.agregar(producto)
        encontrado = self.catalogo.buscar("P1")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Mouse")

    def test_actualizar(self):
        self.catalogo.agregar(Producto("P1", "Mouse", 25))
        self.catalogo.actualizar("P1", "Mouse Gamer", 40)
        producto = self.catalogo.buscar("P1")
        self.assertEqual(producto.nombre, "Mouse Gamer")
        self.assertEqual(producto.precio, 40)

    def test_eliminar(self):
        self.catalogo.agregar(Producto("P1", "Mouse", 25))
        self.catalogo.eliminar("P1")
        self.assertIsNone(self.catalogo.buscar("P1"))
        self.assertNotIn("P1", self.catalogo.codigos)

    def test_duplicado(self):
        self.catalogo.agregar(Producto("P1", "Mouse", 25))
        with self.assertRaises(ValueError):
            self.catalogo.agregar(Producto("P1", "Otro", 30))

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            Producto("P1", "Mouse", -1)


if __name__ == "__main__":
    unittest.main()

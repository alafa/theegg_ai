import unittest

from cuenta import Cuenta

from io import StringIO
import sys


class Capturing(list):

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class NamesTestCase(unittest.TestCase):

    def test_crear_una_cuenta(self):

        unaCuenta = Cuenta("John", 45)
        self.assertEqual(unaCuenta.titular, "John")
        self.assertEqual(unaCuenta.cantidad, 45)

    def test_titular_obligatorio(self):
        # Da error cuando no especificamos titular
        with self.assertRaises(TypeError):
            Cuenta()

    def test_cantidad_no_obligatoria(self):

        # No da error cuando no especificamos cantidad
        try:
            Cuenta("John")
        except Exception:
            self.fail("Cuenta() raised ExceptionType unexpectedly!")

    def test_no_es_posible_modificar_cantidad_directamente(self):

        unaCuenta = Cuenta("John", 45)

        # Da error cuando no intentamos manipular la cantidad
        with self.assertRaises(AttributeError):
            unaCuenta.cantidad = 100000

    def test_cantidad_no_valida(self):

        unaCuenta = Cuenta("John", "hola")
        self.assertEqual(unaCuenta.cantidad, 0)

    def test_ingresar(self):

        unaCuenta = Cuenta("John", 150)

        # Ingresar una cantidad válida
        unaCuenta.ingresar(50)
        self.assertEqual(unaCuenta.cantidad, 200)

        # Ingresar una cantidad no válida (se ignora)
        unaCuenta.ingresar("nada")
        self.assertEqual(unaCuenta.cantidad, 200)

    def test_retirar(self):

        unaCuenta = Cuenta("John", 150)

        # Retirar una cantidad válida
        unaCuenta.retirar(50)
        self.assertEqual(unaCuenta.cantidad, 100)

        # Retirar una cantidad no válida (se ignora)
        unaCuenta.retirar("nada")
        self.assertEqual(unaCuenta.cantidad, 100)

    def test_mostrar(self):

        unaCuenta = Cuenta("John", 45)

        with Capturing() as output:
            unaCuenta.mostrar()

        self.assertEqual('Titular: John', output[0])
        self.assertEqual('Cantidad: 45.0', output[1])


if __name__ == "__main__":

    unittest.main()


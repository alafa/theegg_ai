import unittest

from persona import Persona

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

    def test_crear_una_persona(self):

        unaPersona = Persona("72545123K", "John", 45)
        self.assertEqual(unaPersona.dni, "72545123K")
        self.assertEqual(unaPersona.nombre, "John")
        self.assertEqual(unaPersona.edad, 45)

    def test_argumentos_son_opcionales(self):

        # No da error cuando no especificamos alguno de los parámetros
        try:
            Persona("72545123K", "")
            Persona("", "John", 45)
            Persona(45)

        except Exception:
            self.fail("Persona() raised ExceptionType unexpectedly!")

    def test_validacion_de_parametros(self):

        # DNI no válido
        unaPersona = Persona("34", "John", 45)
        self.assertEqual(unaPersona.dni, "")
        unaPersona = Persona(0, "John", 45)
        self.assertEqual(unaPersona.dni, "")
        unaPersona = Persona("gfgghfghgg", "John", 45)
        self.assertEqual(unaPersona.dni, "")

        # Nombre no válido
        unaPersona = Persona("72545123K", 886, 45)
        self.assertEqual(unaPersona.nombre, "")
        unaPersona = Persona("72545123K", "34", 45)
        self.assertEqual(unaPersona.nombre, "")

        # Edad no válida
        unaPersona = Persona("72545123K", "John", "hola")
        self.assertEqual(unaPersona.edad, "")

        unaPersona = Persona("72545123K", "John", -8)
        self.assertEqual(unaPersona.edad, "")

    def test_mostrar(self):

        unaPersona = Persona("72545123K", "John", 45)

        with Capturing() as output:
            unaPersona.mostrar()

        self.assertEqual('DNI: 72545123K', output[0])
        self.assertEqual('Nombre: John', output[1])
        self.assertEqual('Edad: 45', output[2])

    def test_es_mayor_de_edad(self):

        # Mayor de edad
        unaPersona = Persona("72545123K", "John", 45)
        self.assertEqual(unaPersona.esMayorDeEdad(), True)

        # De 18
        unaPersona = Persona("72545123K", "John", 18)
        self.assertEqual(unaPersona.esMayorDeEdad(), True)

        # Menor de edad
        unaPersona = Persona("72545123K", "John", 17)
        self.assertEqual(unaPersona.esMayorDeEdad(), False)

        # Edad desconocida
        unaPersona = Persona("72545123K", "John")
        self.assertEqual(unaPersona.esMayorDeEdad(), None)

        # Edad no válida
        unaPersona = Persona("72545123K", "John", "esto no es válido")
        self.assertEqual(unaPersona.esMayorDeEdad(), None)

    def test_editar_propiedades(self):

        unaPersona = Persona("72545123K", "John", 45)

        # Ediciones válidas

        unaPersona.dni = "72545333L"
        unaPersona.nombre = "Pepe"
        unaPersona.edad = 33
        self.assertEqual(unaPersona.dni, "72545333L")
        self.assertEqual(unaPersona.nombre, "Pepe")
        self.assertEqual(unaPersona.edad, 33)

        # Ediciones NO válidas (No hay cambio)
        unaPersona.dni = "dni no válido"
        unaPersona.nombre = 34
        unaPersona.edad = -12
        self.assertEqual(unaPersona.dni, "72545333L")
        self.assertEqual(unaPersona.nombre, "Pepe")
        self.assertEqual(unaPersona.edad, 33)




if __name__ == "__main__":

    unittest.main()


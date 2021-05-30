import re


class Persona:

    def __init__(self, dni="", nombre="", edad=""):

        self.dni = dni
        self.nombre = nombre
        self.edad = edad

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, user_input):

        user_input = str(user_input)

        # 8 dígitos + 1 letra
        dni_regex_validation = '^\d{8}[a-zA-Z]$'

        if re.match(dni_regex_validation, user_input):
            self._dni = user_input
        else:
            print("DNI no válido.")

            if not hasattr(self, 'dni'):
                self._dni = ""

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, user_input):

        user_input = str(user_input)

        # Válido cualquier string únicamente con letras y espacios
        name_regex_validation = '^[a-zA-Z\s]*$'

        if re.match(name_regex_validation, user_input):
            self._nombre = user_input
        else:
            print("Nombre no válido.")

            if not hasattr(self, 'nombre'):
                self._nombre = ""

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, user_input):

        # Tiene que ser un número entero positivo
        try:
            if type(int(user_input)) == int:
                if int(user_input) >= 0:
                    self._edad = int(user_input)
                else:
                    print("La edad no puede ser negativa.")
                    if not hasattr(self, 'edad'):
                        self._edad = ""

        except:
            if user_input != "":
                print("Edad no válida.")

            if not hasattr(self, 'edad'):
                self._edad = ""

    def mostrar(self):

        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def esMayorDeEdad(self):

        if self.edad == "":

            print("Edad desconocida.")
            return

        if self.edad >= 18:

            return True
        else:
            return False


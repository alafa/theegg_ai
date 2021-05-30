import re


class Cuenta:

    def __init__(self, titular, cantidad=0):

        self.titular = titular
        self._cantidad = self._validate_cantidad(cantidad)

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, user_input):

        user_input = str(user_input)

        # Válido cualquier string únicamente con letras y espacios
        titular_regex_validation = '^[a-zA-Z\s]*$'

        if re.match(titular_regex_validation, user_input):
            self._titular = user_input
        else:
            print("Nombre de titular no válido.")

            if not hasattr(self, 'titular'):
                self._titular = ""

    @property
    def cantidad(self):
        return round(self._cantidad, 2)

    def _validate_cantidad(self, user_input):

        # Tiene que ser un número entero o decimal
        try:
            if type(float(user_input)) == float:
                return float(user_input)

        except:
            print("Cantidad no válida.")
            return 0

    def mostrar(self):

        print(f"Titular: {self.titular}")
        print(f"Cantidad: {round(self._cantidad, 2)}")

    def ingresar(self, cantidad):

        cantidad_validada = self._validate_cantidad(cantidad)
        self._cantidad = self._cantidad + cantidad_validada

    def retirar(self, cantidad):

        cantidad_validada = self._validate_cantidad(cantidad)
        self._cantidad = self._cantidad - cantidad_validada

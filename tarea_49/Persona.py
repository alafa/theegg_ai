
class Persona:

    def __init__(self, dni="", nombre="", edad=""):

        self.dni = None
        self.nombre = None
        self.edad = None

        self.setDNI(dni)
        self.setNombre(nombre)
        self.setEdad(edad)

    def setDNI(self, dni):

        self.dni = dni

    def setNombre(self, nombre):

        self.nombre = nombre

    def setEdad(self, edad):

        try:
            if type(int(edad)) == int:
                self.edad = int(edad)

        except:
            print("WARNING: Formato de edad incorrecto.")
            self.edad = ""

    def getNombre(self):
        return self.nombre

    def getDNI(self):
        return self.dni

    def getEdad(self):
        return self.edad

    def mostrar(self):

        print(f"Nombre: {self.getNombre()}")
        print(f"DNI: {self.getDNI()}")
        print(f"Edad: {self.getEdad()}")

    def esMayorDeEdad(self):

        if self.edad:
            return self.edad >= 18

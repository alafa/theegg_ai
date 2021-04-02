from collections import Counter
from time import sleep


class Ejercicio1:

    def __init__(self):

        self.numbers = []
        user_input = None

        while user_input != 0:

            print("Inserte un número:")
            user_input_str = input()

            try:
                user_input = int(user_input_str)

                if user_input != 0:
                    self.numbers.append(user_input)

            except:
                print("No es valido. Tiene que introducir un número entero.")

    def remove_number(self):

        print("Introducir número a eliminar:")
        user_input_str = input()

        try:
            user_input = int(user_input_str)
            self.numbers.remove(user_input)

        except:
            print("No se eliminó ningún elemento.")

    def print_sum(self):

        print(f"El sumatorio de todos los elementos es: {sum(self.numbers)}")

    def create_list_with_low_numbers(self):

        user_input_not_valid = True
        while user_input_not_valid:

            print("Inserte un número que hará de tope:")
            user_input_str = input()

            try:

                user_input = int(user_input_str)
                user_input_not_valid = False

                # Crear nueva lista con valores menores al número insertado por usuario
                self.numbers_low = []
                for num in self.numbers:

                    if num < user_input:

                        self.numbers_low.append(num)

                # Imprimir números menores que el número introducido
                print(f"Los números que están por debajo del {user_input} son:")
                for num in self.numbers_low:
                    print(num)

            except:
                print("No es valido. Tiene que introducir un número entero.")

    # Imprimir los números junto con el número de veces que se repiten en la lista
    def print_element_freq(self):

        print("La frecuencia con la que aparecen los números es:")
        print(Counter(self.numbers).most_common())

        sidenote = """
            *Nota: En el enunciado no está claro si este paso se debe realizar con la lista original o con la
                    reducida del paso anterior. Yo he escogido hacerlo con la lista original.
        """
        print(sidenote)


if __name__ == "__main__":

    instance = Ejercicio1()
    print(instance.numbers)
    sleep(1)

    instance.remove_number()
    print(instance.numbers)
    sleep(1)

    instance.print_sum()
    sleep(1)

    instance.create_list_with_low_numbers()
    sleep(1)

    instance.print_element_freq()
    sleep(1)


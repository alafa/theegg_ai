from time import sleep

class Ejercicio2:

    def __init__(self):

        self.primary_students = []
        self.secondary_students = []

        # Recoger nombres del nivel primario
        print("Inserte uno a uno los nombres de los alumnos del nivel primario.")
        print("Inserte \"x\" para finalizar.")
        user_input = ''
        while user_input.lower() != "x":

            user_input = input()

            if user_input.lower() != 'x':
                self.primary_students.append(user_input)

        # Recoger nombres del nivel secundario
        print("Inserte uno a uno los nombres de los alumnos del nivel secundario.")
        print("Inserte \"x\" para finalizar.")
        user_input = ''
        while user_input.lower() != "x":

            user_input = input()

            if user_input.lower() != 'x':
                self.secondary_students.append(user_input)

    def print_names_without_repetitions(self):

        print("\nLos nombres de los alumnos son:")
        print(f"NIVEL PRIMARIO: {', '.join(set(self.primary_students))}")
        print(f"NIVEL SECUNDARIO: {', '.join(set(self.secondary_students))}")

    def print_repeated_names_in_both_levels(self):

        print("\nLos nombres de estudiantes que se repiten en ambos niveles son:")
        exist_repeated = False
        for primary_student in set(self.primary_students):

            if primary_student in self.secondary_students:
                print(primary_student)
                exist_repeated = True

        if not exist_repeated:
            print("No hay nombres que se repitan.")

    def print_unique_students_from_primary_level(self):

        print("\nLos nombres de estudiantes del primer nivel que NO se repiten en el secundario son:")
        exist_unique = False
        for primary_student in set(self.primary_students):

            if primary_student not in self.secondary_students:
                print(primary_student)
                exist_unique = True

        if not exist_unique:
            print("No hay nombres que sean únicos en el nivel primario.")


if __name__ == "__main__":

    # 1. Inicializar instancia recogiendo la información del usuario
    instance = Ejercicio2()
    sleep(1)

    # 2. Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
    instance.print_names_without_repetitions()
    sleep(1)

    # 3. Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
    instance.print_repeated_names_in_both_levels()
    sleep(1)

    #4. Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
    instance.print_unique_students_from_primary_level()



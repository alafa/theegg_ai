from quickSort import QuickSort

class BinarySearch(QuickSort):

    def __init__(self, num_list, itemToSeach):

        self.itemToSeach = itemToSeach

        # Primero ordenamos
        QuickSort.__init__(self, num_list)
        self.moves_to_sort = self.counter

        # Iniciamos variables para la búsqueda
        self.found = False
        self.counter = 0

        # Después buscamos el elemento en la lista aplicando el algoritmo de búsqueda binaria
        self.search()

        # Dar resultados
        self.printResults()

    def search(self):

        i = int(len(self.sorted_list)) - 1

        while not self.found:
            self.counter += 1
            if self.sorted_list[i] == self.itemToSeach:
                print(f"Encontrado en la posición {i}")
                self.found = True

            elif self.sorted_list[i] > self.itemToSeach:

                new_i = int(i / 2)

            else:
                new_i = i + int(i / 2)

            if new_i == i:
                break
            else:
                i = new_i

    def printResults(self):

        if self.found:
            print("Elemento encontrado!")
        else:
            print("Elemento NO encontrado")

        print("Se han necesitado:")
        print(f"{self.moves_to_sort} pasos para odenar la lista")
        print(f"{self.counter} pasos para buscar el elemento")
        print(f"Un total de {self.moves_to_sort + self.counter} pasos.")


number_list = [50, 3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56, -2]
myBinarySearch = BinarySearch(number_list, 33)
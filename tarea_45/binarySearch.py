from quickSort import QuickSort

class BinarySearch(QuickSort):

    def __init__(self, num_list, itemToSeach):

        self.itemToSeach = itemToSeach

        # Primero ordenamos
        QuickSort.__init__(self, num_list)
        self.moves_to_sort = self.counter

        # Iniciamos variables para la búsqueda
        self.found = False
        self.found_position = None
        self.counter = 0

        # Después buscamos el elemento en la lista aplicando el algoritmo de búsqueda binaria
        self.search()

    def search(self):

        min_i = 0
        max_i = len(self.sorted_list)

        while not self.found:

            self.counter += 1
            mid_i = min_i + int((max_i - min_i) / 2)

            if self.sorted_list[mid_i] == self.itemToSeach:
                self.found = True
                self.found_position = mid_i

            elif self.sorted_list[mid_i] > self.itemToSeach:
                # El nº a buscar es menor que el número en mid_i
                max_i = mid_i

            else:
                # El nº a buscar es mayor  que el número en mid_i
                min_i = mid_i

            if min_i == max_i:
                break

    def print_result(self):

        if self.found:
            print(f'Elemento encontrado en posicion {self.found_position}.')
            print(f'Han hecho falta {self.moves_to_sort + self.counter} pasos.')
            print(f'Si la lista hubiera estado ordenada se hubieran necesitado {self.counter} pasos.')

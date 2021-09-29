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

    def search(self):

        min_i = 0
        max_i = len(self.sorted_list)

        while not self.found:

            self.counter += 1
            mid_i = min_i + int((max_i - min_i) / 2)

            if self.sorted_list[mid_i] == self.itemToSeach:
                self.found = True

            elif self.sorted_list[mid_i] > self.itemToSeach:
                # El nº a buscar es menor que el número en mid_i
                max_i = mid_i

            else:
                # El nº a buscar es mayor  que el número en mid_i
                min_i = mid_i

            if min_i == max_i:
                break

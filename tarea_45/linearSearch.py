
class LinearSearch:

    def __init__(self, num_list, itemToSeach):

        self.itemToSeach = itemToSeach

        # Iniciamos variables para la búsqueda
        self.my_List = num_list
        self.found = False
        self.counter = 0

        # Después buscamos el elemento en la lista aplicando el algoritmo de búsqueda binaria
        self.search()

    def search(self):

        for i, num in enumerate(self.my_List):
            self.counter += 1
            if self.itemToSeach == num:
                self.found = True
                break

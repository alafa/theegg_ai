
class LinearSearch:

    def __init__(self, num_list, itemToSeach):

        self.itemToSeach = itemToSeach

        # Iniciamos variables para la búsqueda
        self.my_List = num_list
        self.found = False
        self.found_position = None
        self.counter = 0

        # Se busca el elemento en la lista aplicando el algoritmo de búsqueda linear
        self.search()

    def search(self):

        for i, num in enumerate(self.my_List):
            self.counter += 1
            if self.itemToSeach == num:
                self.found = True
                self.found_position = i
                break

    def print_result(self):

        if self.found:
            print(f'Elemento encontrado en posicion {self.found_position}.')
            print(f'Han hecho falta {self.counter} pasos.')

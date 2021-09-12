
class LinearSearch():

    def __init__(self, num_list, itemToSeach):

        self.itemToSeach = itemToSeach

        # Iniciamos variables para la búsqueda
        self.my_List = num_list
        self.found = False
        self.counter = 0

        # Después buscamos el elemento en la lista aplicando el algoritmo de búsqueda binaria
        self.search()

        # Dar resultados
        self.printResults()

    def search(self):

        for i, num in enumerate(self.my_List):
            self.counter += 1
            if self.itemToSeach == num:
                self.found = True
                break

    def printResults(self):

        if self.found:
            print("Elemento encontrado!")
        else:
            print("Elemento NO encontrado")

        print(f"Un total de {self.counter} pasos.")


number_list = [50, 3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56, -2]
LinearSearch = LinearSearch(number_list, 33)
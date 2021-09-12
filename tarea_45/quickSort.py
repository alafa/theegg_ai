# Se ha implementado el algoritmo de ordenación 'quickSort'

class QuickSort:

    def __init__(self, num_list):

        self.original_list = num_list.copy()
        self.list_size = len(num_list)
        self.counter = 0

        # Comenzar con la ordenación
        self.sorted_list = self.sort(num_list)

    def sort(self, num_list):

        self.counter += 1

        if len(num_list) < 2:

            # Una lista de 0 o 1 elementos está ordenada siempre
            return num_list

        else:

            pivot_num = num_list[0]

            smaller_part = [num for num in num_list[1:] if num < pivot_num]
            bigger_part = [num for num in num_list[1:] if num >= pivot_num]

            # Se llama a la función recursivamente
            return self.sort(smaller_part) + [pivot_num] + self.sort(bigger_part)

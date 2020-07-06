import sys

# Función para encontrar el MCD de dos números
def get_greatest_common_divisor(numbers_array):

    # Función para encontrar divisores de un número
    def get_divisors_of_num(num):
        return [i for i in range(2, num + 1) if num % i == 0]

    divisors = []
    for num in numbers_array:
        divisors.append(get_divisors_of_num(num))

    # Devolver divisores comunes
    common_divs = set.intersection(*[set(list) for list in divisors])
    if len(common_divs) == 0:
        return 1
    else:
        return max(list(common_divs))


class ArgumentError(Exception):

    def __init__(self, *args):

        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ArgumentError, {}'.format(self.message)
        else:
            return 'ArgumentError has been raised.'


class MilkMaximizer:

    def __init__(self, data, max_weight):

        self.max_weight = max_weight
        self.data = data.copy()
        self.whiteboard = []

        self.cow_weights = []
        self.set_list_of_weights()

        self.cow_min_weight = min(self.cow_weights)
        self.gcd = get_greatest_common_divisor(self.cow_weights)

        desired_range = range(1, self.max_weight + self.gcd, self.gcd)
        self.whiteboard_cols_dict = {w: i for i, w in enumerate(desired_range)}

        self.init_whiteboard()

    def set_list_of_weights(self):

        for cow in self.data:
            self.cow_weights.append(cow['weight'])

    def init_whiteboard(self):

        self.whiteboard.append([])
        obj = {
            'liters': 0,
            'weight': 0
        }
        self.whiteboard[0] = [obj] * len(self.whiteboard_cols_dict.keys())

    def getMaxMilk(self):
        for cow_i, cow in enumerate(self.data):
            self.whiteboard.append(list(self.consider_one_more_cow(cow_i)))

        return self.whiteboard[-1][-1]['liters']

    def consider_one_more_cow(self, iter_num):

        cow_to_consider = self.data[iter_num]

        for i, max_weight_to_consider in enumerate(self.whiteboard_cols_dict.keys()):

            # Mejor solución hasta ahora para un camión de i unidades de peso
            best_sol_so_far = self.whiteboard[iter_num][i]

            # Calculamos la capacidad restante que tendriamos si seleccionamos esta vaca
            weight_left = max_weight_to_consider - cow_to_consider['weight']

            # Si el espacio restante es negativo es que la vaca pesa demasiado y seguimos con la misma "best solution so far"
            if weight_left < 0:
                yield best_sol_so_far

            # Si no, tenemos que comprobar si metiendo esta vaca + la mejor solución para el peso restante
            # es mejor que la mejor solucion hasta ahora para la actual capacidad
            else:

                hipotetic_solution = {
                    'liters': cow_to_consider['liters'],
                    'weight': cow_to_consider['weight']
                }

                if weight_left > 0:
                    # Miramos en nuestra chuleta cual era la mejor solucion para weight_left
                    index_to_look = self.whiteboard_cols_dict[weight_left]
                    hipotetic_solution['liters'] = hipotetic_solution['liters'] + self.whiteboard[iter_num][index_to_look]['liters']
                    hipotetic_solution['weight'] = hipotetic_solution['weight'] + self.whiteboard[iter_num][index_to_look]['weight']

                # Comprobamos si esta solución es mejor que ya teniamos
                if hipotetic_solution['liters'] > best_sol_so_far['liters']:
                    yield hipotetic_solution
                else:
                    yield best_sol_so_far


def execute(cow_num, max_weight, weights_list, liters_list):
    data = []
    for i in range(0, cow_num):

        weight = int(weights_list[i])
        liters = int(liters_list[i])

        # Solo tenemos en cuenta la vaca si entra en el camión
        if weight <= max_weight:
            data.append({
                'id': i,
                'weight': weight,
                'liters': liters
            })

    app = MilkMaximizer(data, max_weight)
    result = app.getMaxMilk()
    print(result)


if __name__ == "__main__":

    if len(sys.argv) < 5:
        raise ArgumentError

    cow_num = int(sys.argv[1])
    max_weight = int(sys.argv[2])
    weights_list = sys.argv[3].split(',')
    liters_list = sys.argv[4].split(',')

    execute(cow_num, max_weight, weights_list, liters_list)

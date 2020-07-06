import timeit

from recursive_solution import app as recursive_solution
from dynamic_programming_solution import app as dynamic_programming_solution


def execute_solutions(cows_weights, cows_milk, max_weight):

    print('-> Testing {} cows with {} uniqueg values of weight'.format(len(cows_weights), len(set(cows_weights))))

    print('Recursive solution:')

    ini_time = float(timeit.default_timer())
    recursive_solution.execute(len(cows_weights), max_weight, cows_weights, cows_milk)
    end_time = float(timeit.default_timer())

    print('Runtime: {:.3f} seconds'.format(end_time - ini_time))

    print('Dynamic programming solution:')

    ini_time = float(timeit.default_timer())
    dynamic_programming_solution.execute(len(cows_weights), max_weight, cows_weights, cows_milk)
    end_time = float(timeit.default_timer())

    print('Runtime: {:.3f} seconds'.format(end_time - ini_time))
    print('\n\n')



# Primera prueba: 10 vacas
cows_weights = [35, 20, 40, 27, 41, 23, 5, 16, 18, 16]
cows_milk = [5, 15, 13, 21, 17, 10, 11, 15, 21, 18]
max_weight = 50

execute_solutions(cows_weights, cows_milk, max_weight)

# Segunda prueba: 20 vacas
cows_weights = [35, 21, 40, 27, 41, 23, 5, 16, 18, 17, 35, 20, 40, 23, 41, 20, 5, 16, 18, 19]
cows_milk = [5, 15, 13, 21, 17, 10, 11, 15, 21, 18, 6, 7, 14, 21, 17, 11, 11, 14, 21, 20]
max_weight = 100

execute_solutions(cows_weights, cows_milk, max_weight)

# Tercera prueba: 40 vacas
cows_weights = [35, 20, 40, 27, 41, 23, 5, 16, 18, 16, 35, 20, 40, 23, 41, 20, 5, 16, 18, 19, 35, 20, 40, 27, 41, 23, 5, 16, 18, 14, 35, 20, 40, 23, 41, 20, 5, 16, 18, 18]
cows_milk = [5, 15, 13, 21, 17, 10, 11, 15, 21, 18, 6, 7, 14, 21, 17, 11, 11, 14, 21, 20,5, 15, 13, 21, 17, 10, 11, 15, 21, 18, 6, 7, 14, 21, 17, 11, 11, 14, 21, 20]
max_weight = 150

execute_solutions(cows_weights, cows_milk, max_weight)


# Tercera prueba: 40 vacas con más valores únicos de peso
cows_weights = [35, 20, 40, 27, 41, 23, 4, 16, 21, 16, 36, 22, 40, 23, 42, 20, 5, 16, 18, 19, 33, 20, 38, 27, 41, 23, 6, 17, 18, 14, 34, 21, 37, 23, 39, 16, 5, 16, 18, 19]
cows_milk = [5, 15, 13, 21, 17, 10, 11, 15, 21, 18, 6, 7, 14, 21, 17, 11, 11, 14, 21, 20, 5, 15, 13, 21, 17, 10, 11, 15, 21, 18, 6, 7, 14, 21, 17, 11, 11, 14, 21, 20]
max_weight = 150

execute_solutions(cows_weights, cows_milk, max_weight)



import sys


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
        self.original_data = data.copy()

        self.iter_count = 0

    def getMaxMilk(self):
        return self.simple_iter(0, self.original_data, self.max_weight)

    def simple_iter(self, liters_acum, data, max_weight_left):

        for i, cow in enumerate(data):

            if cow['weight'] > max_weight_left:
                continue

            return max(self.simple_iter(liters_acum + cow['liters'], data[i+1:], max_weight_left - cow['weight']),
                       self.simple_iter(liters_acum, data[i + 1:], max_weight_left))

        return liters_acum


def execute(cow_num, max_weight, weights_list, liters_list):
    data = []
    for i in range(0, cow_num):
        data.append({
            'id': i,
            'weight': float(weights_list[i]),
            'liters': float(liters_list[i])
        })

    app = MilkMaximizer(data, max_weight)
    result = app.getMaxMilk()
    print(result)


if __name__ == "__main__":

    if len(sys.argv) < 5:
        raise ArgumentError

    cow_num = int(sys.argv[1])
    max_weight = float(sys.argv[2])
    weights_list = sys.argv[3].split(',')
    liters_list = sys.argv[4].split(',')

    execute(cow_num, max_weight, weights_list, liters_list)

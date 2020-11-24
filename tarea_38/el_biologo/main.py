import sys

def get_comparable_strings(s1, s2):
    largest_str = s1
    shortest_str = s2

    if len(s1) < len(s2):
        largest_str = s2
        shortest_str = s1

    # Entrando
    for i in range(len(shortest_str)):
        yield largest_str[0:i+1], shortest_str[-i-1:]

    # Se desplaza dentro
    for i in range(len(largest_str) - len(shortest_str)):
        yield largest_str[i+1: i+1 + len(shortest_str)], shortest_str

    # Saliendo
    for i in range(len(shortest_str) - 1):
        yield largest_str[-len(shortest_str) + 1 + i:], shortest_str[0:len(shortest_str) - 1 -i]


# s1 and s2 should be same size
def common_string(s1, s2):
    common_strings = []
    common_str = ''

    for pair_of_chars in list(zip(s1, s2)):
        if pair_of_chars[0] == pair_of_chars[1]:
            common_str = common_str + pair_of_chars[0]
        else:
            common_strings.append(common_str)
            common_str = ''

    common_strings.append(common_str)
    if common_strings:
        return max(common_strings, key=len)
    else:
        return ''


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print('ERROR: No se encuentran suficientes argumentos.')
        exit()

    max_length = 0
    common_strings = []
    for pair in get_comparable_strings(sys.argv[1], sys.argv[2]):
        s = common_string(pair[0], pair[1])
        common_strings.append(s)
        if len(s) > max_length:
            max_length = len(s)

    for res in common_strings:
        if len(res) == max_length:
            print(res)

import sys

# Devuelve True si es un número palíndromo
def check_if_palindromo(num):

    num_str = str(num)
    for i in range(0, int(len(num_str)/2)):
        if num_str[i] != num_str[-i-1]:
            return False
    return True


# Devuelve True si es un número primo
def check_if_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


# Devuelve el siguiente número primo y palindromo al número proporcionado
def get_next_palindrome_and_prime(num):

    while True:

        if check_if_palindromo(num) and check_if_prime(num):
            return num

        num = num + 1


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('ERROR: Se debe proporcionar un número entero como argumento.')
        exit()

    try:
        num = int(sys.argv[1])

    except:
        print('ERROR: Se debe proporcionar un número entero como argumento.')
        exit()

    res = get_next_palindrome_and_prime(num)
    print(res)
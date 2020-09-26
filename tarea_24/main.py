import sys

# Convierte un número decimal a binario
def dec_to_binary(dec_num):

    def recursive_func(num, tmp=''):

        if num > 1:
            tmp = recursive_func(num // 2, tmp)
        return tmp + str(num % 2)

    return recursive_func(dec_num)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('No se encuentra argumento.')
        exit()

    try:
        num_dec = int(sys.argv[1])
    except:
        print("Lo que se ha proporcionado como argumento no es un número decimal")
        exit()

    binary_num = dec_to_binary(num_dec)
    print(binary_num)

from time import time


def suma_lineal(n):

    sum = 0
    for i in range(n+1):
        sum += i

    return sum


def suma_constante(n):

    return int((n/2) * (n+1))


if __name__ == "__main__":

    N = 1000000

    for i in range(4):

        t0 = time()
        suma1 = suma_lineal(N)
        t1 = time()

        suma2 = suma_constante(N)
        t2 = time()

        print(f"Para N={N}")
        print(f"Suma lineal: {suma1}       -    temp: {t1-t0}")
        print(f"Suma constante: {suma2}    -    temp: {t2-t1}")
        print("-----------------------------------------------------")

        N *= 10
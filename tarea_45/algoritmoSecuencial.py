

if __name__ == "__main__":

    number_list = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
    number_to_find = 874

    found = False
    steps = 0

    for i, num in enumerate(number_list):
        steps += 1
        if number_to_find == num:

            print(f"Encontrado en posición {i}")
            found = True
            break

    if not found:
        print("No encontrdado")

    print(f"Pasos realizados: {steps}")


def encontrarNumeroConAlgoritmoSecuencial(list, item_to_find):

    found = False
    steps = 0

    for i, num in enumerate(list):
        steps += 1
        if item_to_find == num:
            found = True
            break

    if found:
        print("No encontrado")
    else:
        print("No encontrado")

    print(f"Pasos realizados: {steps}")


if __name__ == "__main__":

    number_list = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
    number_to_find = 874

    encontrarNumeroConAlgoritmoSecuencial(number_list, number_to_find)


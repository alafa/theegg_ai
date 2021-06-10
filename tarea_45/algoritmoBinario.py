
def encontrarNumeroConAlgoritmoBinario(list, item_to_find):

    list.sort()

    found = False
    steps = 0
    i = int(len(list)) -1

    while not found:
        steps += 1
        if list[i] == item_to_find:
            print(f"Encontrado en la posición {i}")
            found = True

        elif list[i] > item_to_find:

            new_i = int(i / 2)

        else:
            new_i = i + int(i / 2)

        if new_i == i:
            break
        else:
            i = new_i

    if found:
        print("Encontrado!")
    else:
        print("No encontrado")

    print(f"Pasos realizados: {steps}")


if __name__ == "__main__":

    number_list = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
    number_to_find = 874

    encontrarNumeroConAlgoritmoBinario(number_list, number_to_find)


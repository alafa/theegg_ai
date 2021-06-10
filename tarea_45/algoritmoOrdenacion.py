
# Swap function
def swapPositions(mylist, pos1, pos2):
    mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]
    return mylist

def ordenar_lista(mylist):

    i = 1
    while i < len(mylist):

        if mylist[i-1] > mylist[i]:
            mylist = swapPositions(mylist, i, i-1)
            i = 1
        else:
            i += 1

    print(mylist)


if __name__ == "__main__":

    number_list = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
    ordenar_lista(number_list)

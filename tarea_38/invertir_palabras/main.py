import sys


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('ERROR: Tienes que proporcionar la frase')
        exit()
    elif len(sys.argv) > 2:
        print("ERROR: Asegurate de envolver la frase entre comillas dobles.")
        exit()

    words = sys.argv[1].split(' ')
    inverse_sentence = []
    for i in range(len(words) - 1, -1, -1):
        inverse_sentence.append(words[i])

    print(' '.join(inverse_sentence))

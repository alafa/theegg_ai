import sys


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('ERROR: Tienes que proporcionar el número de frases que se quiere invertir')
        exit()

    try:
        num_sentences = int(sys.argv[1])
    except:
        print('ERROR: El argumento debe ser un número entero')
        exit()

    results = []

    for i in range(0, num_sentences):

        print('')
        print(f"#{i+1} Escribe una frase y presiona enter:")
        sentence_input = input()
        words = sentence_input.split(' ')
        inverse_sentence = []
        for i in range(len(words) - 1, -1, -1):
            inverse_sentence.append(words[i])

        results.append(' '.join(inverse_sentence))

    print("\nFRASES INVERTIDAS:")
    for i, result in enumerate(results):
        print(f"#Case {i+1}: {result}")

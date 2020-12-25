import re

if __name__ == "__main__":
    f = open("./text.txt", "r", encoding='utf-8')
    text = f.read()

    print("\n --> Número total de carácteres en el texto:")
    chars_in_text = re.findall(".", text)
    print(len(chars_in_text))

    print("\n --> Número total de palabras en el texto:")
    words_in_text = re.findall("\w+", text)
    print(len(words_in_text))

    # Inicializar el contador de palabras a 1
    word_count = {}

    # Se itera por cada palabra encontrada y para cada una se busca, ignorando mayúsculas y minusculas, cuantas
    # veces aparece en el texto y se guarda en el diccionario.
    for word in list(words_in_text):

        word_count[word.lower()] = len(re.findall(f"\\b{word}\\b", text, re.IGNORECASE))

    ranking_count_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    print("\n --> Ranking de las palabras más frecuentes:")
    for w in ranking_count_words:
        print(f"{w[0]}: {w[1]}")
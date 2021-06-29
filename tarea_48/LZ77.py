class LZ77:

    def __init__(self, message):

        print(f"Tamaño del mensaje original: {len(message)}")

        self.encript_dict = {}
        self.encripted_msg = ""

        c = 0
        for word in set(message.split(" ")):
            self.encript_dict[word] = c
            c += 1

        self.comprimir_mensaje(message)
        print(f"Tamaño del mensaje comprimido: {len(self.encripted_msg)}")
        print(f"Mensaje comprimido: {self.encripted_msg}")


    def comprimir_mensaje(self, msg):

        encripted_values = []
        for word in msg.split(" "):
            encripted_values.append(str(self.encript_dict[word]))

        self.encripted_msg = ' '.join(encripted_values)

    def descomprimir_mensaje(self):

        resulted_words = []
        for index in self.encripted_msg.split(' '):
            resulted_words.append(list(self.encript_dict.keys())[int(index)])

        print(f"Mensaje descomprimido: {' '.join(resulted_words)}")

def pedir_mensaje():

    return input("Inserte el mensaje a encriptar (max 30 carácteres) o presiona Enter para encriptar el mensaje ejemplo (\"sueño que tengo sueño\"):")


if __name__ == "__main__":

    default_msg = "sueño que tengo sueño"
    msg = pedir_mensaje()

    while len(msg) > 30:
        print("Mensaje demasiado largo. No válido. Max 30 caracteres.\n")
        msg = pedir_mensaje()

    if not msg:
        msg = default_msg

    # Creamor nuestra instancia de compresor (algoritmo LZ77)
    compresor = LZ77(msg)

    # Hemos comprimidor el mensaje y ahora queremos descomprimirlo de nuevo
    compresor.descomprimir_mensaje()

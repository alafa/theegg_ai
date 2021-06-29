class LZ77():

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


if __name__ == "__main__":

    #Todo: Input del usuario y max 30 caracteres
    comprimidor = LZ77("sueño que tengo sueño")
    comprimidor.descomprimir_mensaje()
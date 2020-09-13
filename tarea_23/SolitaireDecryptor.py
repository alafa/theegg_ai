import json
from Solitaire import Solitaire


class SolitaireDecryptor(Solitaire):

    def __init__(self, deck):

        # Init call to superclass
        Solitaire.__init__(self, deck)

    def decrypt_msg(self, encrypted_msg):

        # Initialise deck
        self.deck.set_cards_as(self.deck)

        key = self.generate_key(len(encrypted_msg))

        numeric_msg = self.convert_letters_to_nums(encrypted_msg)

        key_msg_difference = [x - y for x, y in zip(numeric_msg, key)]
        key_msg_difference_mod26 = [value + 26 if value < 0 else value for value in key_msg_difference]

        decrypted_msg = self.convert_nums_to_letters(key_msg_difference_mod26)

        return ''.join(decrypted_msg)



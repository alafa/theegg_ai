import json
from SolitaireClass import Solitaire


class SolitaireEncryptor(Solitaire):

    def __init__(self, deck):

        # Init call to superclass
        Solitaire.__init__(self, deck)

    def encrypt_msg(self, msg):

        key = self.generate_key(len(msg))

        numeric_msg = self.convert_letters_to_nums(msg)

        key_msg_sum = [x + y for x, y in zip(key, numeric_msg)]
        key_msg_sum_mod26 = [value - 26 if value > 26 else value for value in key_msg_sum]

        self.encrypted_msg = self.convert_nums_to_letters(key_msg_sum_mod26)

        return ''.join(self.encrypted_msg)



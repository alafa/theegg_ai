import json
from Solitaire import Solitaire


class SolitaireEncryptor(Solitaire):

    def __init__(self, deck):

        # Init call to superclass
        Solitaire.__init__(self, deck)

    def encrypt_msg(self, msg):

        # Remove spaces
        msg = msg.replace(' ', '')

        # Generate key
        key = self.generate_key(len(msg))

        # Convert message to numbers
        numeric_msg = self.convert_letters_to_nums(msg)

        # Sum key + numeric message (mod: 26)
        key_msg_sum = [x + y for x, y in zip(key, numeric_msg)]
        key_msg_sum_mod26 = [value - 26 if value > 26 else value for value in key_msg_sum]

        # Convert result to letters
        res = self.convert_nums_to_letters(key_msg_sum_mod26)

        # Return result as a sting
        return ''.join(res)



from DeckClass import Deck
import json

class Solitaire:

    def __init__(self):

        # Create Deck
        self.original_deck = Deck()

        # Shuffle cards in deck
        self.original_deck.shuffle()

        #  create a copy of the original deck
        self.deck = Deck()

        self.encrypted_msg = None

        # Load the dictionary where letter-number is defined
        with open('letter_conversion.json') as json_file:
            self.letter_conversion_dict = json.load(json_file)

    def get_number_of_key(self):

        # Move back joker A one position
        self.deck.move_card("joker", 'A', 1)

        # Move back joker B two positions
        self.deck.move_card("joker", 'B', 2)

        # Cut he deck in three (by jokers) and swap ends
        self.deck.cut_and_swap_by_jokers()

        # Get first card value
        firstCardvalue = self.deck.get_first_card_value()

        # get card in 'firstCardvalue' position
        chosenCard = self.deck.get_card(firstCardvalue)

        if chosenCard.type == 'joker':
            return None

        else:
            return chosenCard.value

    def generate_key(self, length_of_key):

        key = []
        while len(key) < length_of_key:

            num_of_key = self.get_number_of_key()
            if num_of_key is not None:

                if num_of_key > 26:
                    num_of_key = num_of_key - 26

                key.append(num_of_key)

        return key

    def convert_letters_to_nums(self, letters):

        nums = []
        for letter in letters:
            nums.append(self.letter_conversion_dict[letter.upper()])

        return nums

    def convert_nums_to_letters(self, nums):

        letters = []
        for num in nums:
            for letter_field in self.letter_conversion_dict:
                if self.letter_conversion_dict[letter_field] == num:
                    letters.append(letter_field)

        return letters

    def encrypt_msg(self, msg):

        # Initialise deck
        self.deck.set_cards_as(self.original_deck)

        key = self.generate_key(len(msg))

        numeric_msg = self.convert_letters_to_nums(msg)

        key_msg_sum = [x + y for x, y in zip(key, numeric_msg)]
        key_msg_sum_mod26 = [value - 26 if value > 26 else value for value in key_msg_sum]

        self.encrypted_msg = self.convert_nums_to_letters(key_msg_sum_mod26)

        return ''.join(self.encrypted_msg)

    def decrypt_msg(self):

        if self.encrypted_msg is None:
            print('There is nothing encrypted')
            return

        # Initialise deck
        self.deck.set_cards_as(self.original_deck)

        key = self.generate_key(len(self.encrypted_msg))

        numeric_msg = self.convert_letters_to_nums(self.encrypted_msg)

        key_msg_difference = [x - y for x, y in zip(numeric_msg, key)]
        key_msg_difference_mod26 = [value + 26 if value < 0 else value for value in key_msg_difference]

        decrypted_msg = self.convert_nums_to_letters(key_msg_difference_mod26)

        return ''.join(decrypted_msg)




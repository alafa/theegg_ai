import random

from Card import Card

class DeckOfCards:

    def __init__(self):

        self.cards = []

        card_possible_types = ["clubs", "diamonds", "hearts", "spades"]
        card_possible_nums = [num for num in range(1, 14)]

        for type in card_possible_types:

            for num in card_possible_nums:

                self.cards.append(Card(type, num))

        # Add two Jokers
        self.cards.append(Card("joker", 'A'))
        self.cards.append(Card("joker", 'B'))

    def shuffle(self):

        random.shuffle(self.cards)

    def move_card(self, type, num, positions):

        for i, card in enumerate(self.cards):

            if card.type == type and card.num == num:

                to_move_card_index = i

        to_move_card = self.cards.pop(to_move_card_index)

        # Insert card again in right position
        new_index = to_move_card_index + positions
        if new_index >= len(self.cards):
            new_index = new_index - len(self.cards)

        self.cards = self.cards[0:new_index] + [to_move_card] + self.cards[new_index:]

    def cut_and_swap_by_jokers(self):

        # find jokers
        jokers_index = []
        for i, card in enumerate(self.cards):
            if card.type == "joker":
                jokers_index.append(i)

            if len(jokers_index) == 2:
                break

        # Take the jokers out
        joker1 = self.cards.pop(jokers_index[0])
        joker2 = self.cards.pop(jokers_index[1]-1)

        # Define 3 chunks
        chunk1 = self.cards[0:jokers_index[0]]
        chunk2 = self.cards[jokers_index[0]: jokers_index[1]-1]
        chunk3 = self.cards[jokers_index[1]-1:]

        # Swap: Reorder chunks and include jokers cards
        self.cards = chunk3 + [joker1] + chunk2 + [joker2] + chunk1

    def get_first_card_value(self):

        return self.cards[0].value

    def get_card(self, position):

        return self.cards[position]

    def set_cards_as(self, other_deck):

        self.cards = other_deck.cards.copy()

import sys

from DeckOfCards import DeckOfCards
from SolitaireEncryptor import SolitaireEncryptor
from SolitaireDecryptor import SolitaireDecryptor


if __name__ == "__main__":

    # Get message to escrypt as argument
    if len(sys.argv) < 2:
        print('There is no message to encrypt.')
        exit()

    msg = sys.argv[1]

    # Create two decks
    deck1 = DeckOfCards()
    deck2 = DeckOfCards()

    # Shuffle deck1 and copy cards to deck2
    deck1.shuffle()
    deck2.set_cards_as(deck1)

    # ENCRYTP
    print('Original message: {}'.format(msg))
    encryptor = SolitaireEncryptor(deck1)
    encrypted_msg = encryptor.encrypt_msg(msg)

    print('Encrypted to: {}'.format(encrypted_msg))

    # DECRYPT
    decryptor = SolitaireDecryptor(deck2)
    decripted_msg = decryptor.decrypt_msg(encrypted_msg)

    print('Message decrypted: {}'.format(decripted_msg))

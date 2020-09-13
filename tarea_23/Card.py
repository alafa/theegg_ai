class Card:

    def __init__(self, type, num):

        self.type = None
        self.num = None
        self.value = None

        allowed = False
        if type in ["spades", "diamonds", "hearts", "clubs"]:

            if 0 < num < 14:

                allowed = True

        elif type == "joker" and num in ['A', 'B']:

            allowed = True

        if not allowed:
            print("Card properties not allowed")

        else:

            self.type = type
            self.num = num

            if type == "clubs":

                self.value = num

            elif type == "diamonds":

                self.value = num + 13

            elif type == "hearts":

                self.value = num + 26

            elif type == "spades":

                self.value = num + 39

            else:

                #joker
                self.value = 53
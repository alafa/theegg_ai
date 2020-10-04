import sys


class Pokemon:

    def __init__(self, name, life_points, attack_points):

        self.name = name
        self.life_points = life_points
        self.attack_points = attack_points

    def suffer_damage(self, damage):

        self.life_points = self.life_points - damage

    def is_alive(self):

        if self.life_points > 0:
            return True
        else:
            return False


def announce_winner(winner):

    print("{} wins!".format(winner.name))


def fight(pok1, pok2):

    pok1_turn = True
    round = 0

    while pok1.is_alive() and pok2.is_alive():

        round = round + 1

        if pok1_turn:
            pok2.suffer_damage(pok1.attack_points)

        else:
            pok1.suffer_damage(pok2.attack_points)

        pok1_turn = not pok1_turn

    if pok1.is_alive():
        announce_winner(pok1)
    else:
        announce_winner(pok2)


if __name__ == "__main__":

    if len(sys.argv) < 5:
        print('No se encuentran suficientes argumentos.')
        exit()

    pikachu_life_points = int(sys.argv[1])
    pikachu_attack_points = int(sys.argv[2])
    jigglipuff_life_points = int(sys.argv[3])
    jigglipuff_attack_points = int(sys.argv[4])

    pikachu = Pokemon("Pikachu", pikachu_life_points, pikachu_attack_points)
    jigglipuff = Pokemon("Jigglipuff", jigglipuff_life_points, jigglipuff_attack_points)

    fight(pikachu, jigglipuff)


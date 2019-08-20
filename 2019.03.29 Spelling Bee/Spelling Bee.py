import random as r
import matplotlib.pyplot as plt


class SpellingBeeContenstant():
    _knowledge = 0
    _name = "You Fucked Up"

    def __init__(self, percentage_knowledge):
        self._knowledge = percentage_knowledge

    def get_knowledge(self):
        return self._knowledge

    def __str__(self):
        return str(self._knowledge)


def setup_spelling_bee():
    players = []
    for i in range(90,100):
        players.append(SpellingBeeContenstant(i))
    return players


def test_player(player : SpellingBeeContenstant):
    return player.get_knowledge() >= r.randint(1,100)


def run_spelling_bee():
    players = setup_spelling_bee()

    while True:
        for player in players:
            if not test_player(player):
                players.remove(player)
            if len(players) == 1:
                return players[0]


def simulate_several_bees(amount):
    wincount = [0 for i in range(10)]
    for i in range(amount):
        wincount[run_spelling_bee().get_knowledge() - 90] += 1
    return [x / amount for x in wincount]


def graph_wins(win_count_list : list):
    labels = [str(i) for i in range(90, 100)]
    winpct = win_count_list

    plt.bar(labels, winpct)
    plt.ylabel('Win Share')
    plt.title('Win Share by incrementing order')
    plt.show()

graph_wins(simulate_several_bees(10000))
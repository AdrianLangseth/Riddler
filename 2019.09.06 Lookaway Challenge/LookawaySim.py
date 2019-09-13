import numpy.random as r
import matplotlib.pyplot as plt

# directions = ["up", "right", "down", "left"]

def lookaway():
    player = 0
    while True:


        r1 = r.randint(4)
        r2 = r.randint(4)

        if r1 == r2:
            return player
        else:
            player += 1
            player = player % 2


def simManyLookaway(n):
    player1_wins = 0
    games = 0
    playerwinlist = []
    gamelist = [i for i in range(1, n+1 )]
    for i in range(n):
        games = games + 1
        result = lookaway()
        if result == 0:
            player1_wins += 1
        playerwinlist.append(player1_wins)
    plt.plot(playerwinlist, gamelist)
    plt.show()
    return player1_wins / games


print(simManyLookaway(10000000))


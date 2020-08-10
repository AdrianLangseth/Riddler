import random as r
KaspWinProp = 3/48
KarpWinProb = 5/48


def sim(karpov_start = 0, kasparov_start = 0):
    karpov_win = karpov_start
    kasparov_win = kasparov_start
    while True:
        if karpov_win == 6:
            return "karpov"
        if kasparov_win == 6:
            return "kasparov"

        i = r.randint(1, 48)
        if i < 4:
            kasparov_win += 1
        elif i < 9:
            karpov_win += 1



def run_simulations(n, karp = 0, kasp = 0):
    kasp_games = 0
    karp_games = 0
    for i in range(n):
        winner = sim(karp, kasp)
        if winner == "karpov":
            karp_games += 1
            continue
        elif winner == "kasparov":
            kasp_games += 1
            continue

    kasp_prob = kasp_games/n
    karp_prob = karp_games/n

    return karp_prob, kasp_prob


print(run_simulations(100000000, 5, 3))
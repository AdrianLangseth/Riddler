import random as r



def coffecardSimulation():
    wallet = [50, 50]
    while True:
        num = r.randint(0,1)
        if wallet[num] == 0:
            return wallet[1-num]
        else:
            wallet[num] -= 1



def simulateCoffeProbability(n):
    probability_of_coffee = 0
    expected_coffee = 0
    for i in range(n):
        cupsleft = int(coffecardSimulation())
        if cupsleft != 0:
            expected_coffee += cupsleft
            probability_of_coffee += 1
    expected_coffee = expected_coffee / n
    probability_of_coffee = probability_of_coffee / n
    return round(probability_of_coffee, 3), round(expected_coffee)

print(simulateCoffeProbability(1000))
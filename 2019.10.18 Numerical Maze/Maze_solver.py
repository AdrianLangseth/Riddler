from Maze import build_matrix


def dynamic_solve(mazeMatrix: list, start: tuple, end: tuple):
    """
    Solves maze dynamically
    :param mazeMatrix: The maze to be solved
    :param start: Start on [x][y] form in tuple (x,y)
    :param end: end on [x][y] form in tuple (x,y)
    :return:
    """

    maze = mazeMatrix
    startX, startY = start
    weight = maze[startX][startY]
    children = check_all_sides(maze, (startX, startY))
    while True:
        succ = []
        for i in children:
            if i == end:
                return True
            else:
                succ.append(check_all_sides(maze, i))
        children = succ



def check_all_sides(maze: list, pos: tuple):
    x, y = pos
    possibilities = []
    # check_horizontal
    for i in range(10):
        if i != y:
            if maze[x][i] == abs(y - i):
                possibilities.append(tuple([x,i]))

    # check_veritcal
    for j in range(10):
        if j != x:
            if maze[j][y] == abs(x - j):
                possibilities.append(tuple([j, y]))
    return possibilities


maze = build_matrix()
print(dynamic_solve(maze, (6,2), (9,0)))
# check_all_sides(maze, (6, 2))

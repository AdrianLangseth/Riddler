import matplotlib.pyplot as plt


class Solution():
    def __init__(self, sizebasis: int):
        '''
        Initialize the solution class with an island of 3:2 ratio and basis size of the parameter
        :param sizebasis: basis for the island size
        '''
        self.length = sizebasis * 2
        self.height = sizebasis * 3
        self.island = [[0 for i in range(self.length)] for j in range(self.height)]

    def eval(self) -> None:
        '''
        Evaluate every point on the map and evaluate if the nearest edge is a tie for first.
        :return: None
        '''
        def check_tie(a, b, c, d):
            if [a, b, c, d].count(min([a, b, c, d])) > 1:
                return True

        for i in range(self.height):
            for j in range(self.length):
                left = i
                right = self.height - i
                up = j
                down = self.length - j
                if check_tie(left, right, up, down):
                    self.island[i][j] = 1

    def show(self) -> None:
        '''
        Display the island graphically with evaluation edits.
        :return: None
        '''
        plt.imshow(self.island, cmap='gray')
        plt.show()


# Run
if __name__ == '__main__':
    s = Solution(100)
    s.eval()
    s.show()

print(__name__)

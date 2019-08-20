import numpy as np
import matplotlib.pyplot as plt

def get_odds_matrix_up_to(Amounts):
    """
    calculates a matrix of probability of human victory and returns it
    :param Amounts: the size of the k * k matrix per dimension
    :return croppedOddsMatrix: Matrix of probability for human wins for m humans, n white walkers
    """

    # First we make base matrix with 1 as when no white walkers remain, signifying a human victory.
    oddsmatrix = [[0 for x in range(Amounts * 2)] for y in range(Amounts)] # Must be 2*Amounts to avoid outofboundserror
    oddsmatrix[0][0]= 0.5
    for i in range(1,Amounts):
        oddsmatrix[i][0] = 1

    for humans in range(1, Amounts):
        for whiteWalkers in range(1, Amounts):
            oddsmatrix[humans][whiteWalkers] = (oddsmatrix[humans][whiteWalkers - 1])/2 + (oddsmatrix[humans-1][whiteWalkers + 1])/2


    numpy_oddsmatrix = np.array(oddsmatrix)
    croppedOddsArray = numpy_oddsmatrix[:, :Amounts]  # reshape back into original size.
    return croppedOddsArray


def two_d_list_to_matrix_visualization(two_d_list):
    """
    Takes a 2d list and prints it line by line to visualize it as a matrix rather than a list of lists.
    :param two_d_list: a 2d list
    :return: None
    """
    for i in two_d_list:
        print(i)


def plot_oddsmatrix(oddsmatrix:np.ndarray):
    plt.imshow(oddsmatrix)
    plt.title("Probability Living Army Wins")
    plt.xlabel("Night King Army Size")
    plt.ylabel("Living Army Size")
    plt.savefig("knightking_colormap.pdf")
    plt.colorbar()
    plt.show()



plot_oddsmatrix(get_odds_matrix_up_to(100))
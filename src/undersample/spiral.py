import numpy as np
import math

import matplotlib.pyplot as plt


def chk(x, y, a, b, thickness):
    x = x - a  # changing the center of the spiral to the center of the plot
    y = y - b

    c = 50000

    try:
        if abs(y - x * math.tan(math.sqrt(c / (x ** 2 + y ** 2)))) <= thickness:
            return 1
    except:
        pass

    return 0


def get_spiral(size, thickness, plot=False):
    """
    Method to generate spiral undersampling

    Equation of our spiral:  y = x tan(sqrt(a/(x²+y²) ).

    Parameters
    ----------
    size : list
        size of the array required, for e.g. [250,250]
    thickness : int
        thickness of spirals
    plot : bool, optional
        plots the array if True.
    """
    dimention = size
    a = dimention[0] // 2  # x-coordinate of center(keep it to half of width)
    b = dimention[1] // 2  # y-coordinate of center(keep it to half of height)
    arr = np.zeros(dimention)  # Initializing the array with zeros
    for x in range(dimention[0]):
        for y in range(dimention[1]):
            arr[x][y] = chk(x, y, a, b, thickness)

    if plot:
        plt.imshow(arr)
    return arr

import math
import numpy as np
import matplotlib.pyplot as plt


def dist(x1, y1, x2, y2):
    return math.sqrt(
        (x1 - x2) ** 2 + (y1 - y2) ** 2
    )  # calculate distance between two points


def make_circle(circle, cx, cy, r):
    """
    circle is a 2D list, cx,cy are coordinates of center
    """
    for x in range(cx - r, cx + r):  # x-coordinate will belong to range (cx-r,cx+r)
        for y in range(cy - r, cy + r):  # y-coordinate will belong to range(cy-r,cy+r)
            if dist(cx, cy, x, y) <= r and dist(cx, cy, x, y) >= r - 3:
                circle[x][y] = 1


def get_circles(size, num, plot=False):
    """
    Method to generate circular undersampling

    Parameters
    ----------
    size : tuple
        size of the array required, for e.g. (250,250)
    num : int
        number of circles
    plot : bool, optional
        plots the array if True.
    """
    width = size[0]
    height = size[1]
    diameter = min(size[1], size[0])
    cx = diameter // 2  # x-coordinate of center(keep it to half of width)
    cy = diameter // 2  # y-coordinate of center(keep it to half of height)
    r = diameter // 2  # radius

    circle = [
        [0 for _ in range(width)] for _ in range(height)
    ]  # initializing a 2d list with all pixels set as 0

    number_of_circles = num

    for i in range(number_of_circles):
        make_circle(circle, cx, cy, r - 10 * i)

    circle = np.array(circle)  # converting to numpy array

    if plot:
        plt.imshow(circle)  # plotting the array as an image
    return circle

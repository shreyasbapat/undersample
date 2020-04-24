import matplotlib.pyplot as plt
import numpy as np


def complex_points(z):
    """
    Input:
    ------
    z : Complex Number

    Output:
    -------
    ~Tuple :
           Real and Imaginary part of z, in a tuple, (Re(z), Im(z))

    """
    return (z.real, z.imag)


# From http://floppsie.comp.glam.ac.uk/Southwales/gaius/gametools/6.html
def points(start, end):
    """
    Bresenham's Line Drawing Algorithm in 2D
    """
    l = []
    x0, y0 = start
    x1, y1 = end

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    if x0 < x1:
        sx = 1
    else:
        sx = -1

    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx - dy

    while True:
        l.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err
        if e2 > -dy:
            # overshot in the y direction
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            # overshot in the x direction
            err = err + dx
            y0 = y0 + sy

    return l


def get_radial(dim=250, numradii=20, plot=True):
    """
    Input:
    ------
    dim : int
        Dimensions of the plot array. Defaults to 250.
    numradii : int
             Number of radial lines on the plot. Defaults to 20.
    plot : Boolean
         Plots plot_arr, if True. Defaults to True.

    Output:
    -------
    plot_arr : ~numpy.ndarray
             Array, with the radial plot

    """
    # Initializing as array of 1s
    # "+2" is to have additional space in the final plot
    plot_arr = np.ones((dim + 2, dim + 2))
    # Number of diameters
    numlines = 2 * numradii

    # Sampling points in complex plane and rounding each point off to nearest integer
    sample = np.array(
        [
            complex_points((dim // 2) * np.exp(1j * th))
            for th in np.linspace(0, 2 * np.pi, numlines, endpoint=False)
        ]
    )
    rounded_sample = np.ndarray.astype(np.round(sample), dtype=int)

    # Stores radii endpoints to optimize line drawing
    lst_ends = []
    for i, j in rounded_sample:
        # Setting radii endpoints to 0 in plot_arr
        # "(dim//2) + 1" appears because of translation of each point into the first cartesian quadrant
        plot_arr[i + (dim // 2) + 1, j + (dim // 2) + 1] = 0
        lst_ends.append((i + (dim // 2) + 1, j + (dim // 2) + 1))

    # To visualize the endpoints
    # if plot:
    # plt.figure(figsize=(10,10))
    # plt.imshow(plot_arr, cmap='gray')
    # plt.tick_params(labelbottom=False, labeltop=True)

    # Modifying lst_ends to make things simpler
    lst_ends = np.array(
        [lst_ends[: len(lst_ends) // 2], lst_ends[len(lst_ends) // 2 :]]
    )

    # List of paths for each pair of end-points
    path_list = [points(lst_ends[0, j], lst_ends[1, j]) for j in range(numlines // 2)]

    # Modifying plot_arr
    for path in path_list:
        for i, j in path:
            plot_arr[i, j] = 0

    # Plotting plot_arr
    if plot:
        plt.figure(figsize=(10, 10))
        plt.imshow(plot_arr, cmap="gray")
        plt.tick_params(labelbottom=False, labeltop=True)

    return plot_arr

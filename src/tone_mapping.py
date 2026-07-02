import numpy as np


def linear(rgb):

    return np.clip(rgb, 0, 1)


def reinhard(rgb):

    return rgb / (1 + rgb)


def aces(rgb):

    a = 2.51
    b = 0.03
    c = 2.43
    d = 0.59
    e = 0.14

    rgb = (rgb * (a * rgb + b)) / (rgb * (c * rgb + d) + e)

    return np.clip(rgb, 0, 1)
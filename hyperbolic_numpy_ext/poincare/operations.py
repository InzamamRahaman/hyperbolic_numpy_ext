import numpy as np
import numba
import numpy.linalg as linalg
from typing import Union


def h_dist(x: np.array, y: np.array) -> Union[float, np.float]:
    """
    Calculates the hyperbolic distance between two numpy arrays in the Poincaré ball model of hyperbolic space
    :param x: the first vector
    :param y: the second vector
    :return: the distance between vectors x and y
    """

    nx = 1 - np.power(linalg.norm(x, axis=1), 2)
    ny = 1 - np.power(linalg.norm(y, axis=1), 2)
    denom = nx * ny

    numer = np.power(linalg.norm(x - y), 2)
    frac = 2 * numer / denom
    inner = 1 + frac
    res = np.cosh(inner)
    return res


def h_add(x: np.array, y: np.array, c=1.0) -> np.array:
    norm_x_sqrd = np.power(linalg.norm(x, axis=1), 2)
    norm_y_sqrd = np.power(linalg.norm(y, axis=1), 2)
    inner_prod_of_x_y = np.diag(np.dot(x, np.transpose(y)))

    denom = 1 + 2 * c * inner_prod_of_x_y + c * c * norm_x_sqrd * norm_y_sqrd
    numer_p_1 = (1 + 2 * c * inner_prod_of_x_y + c * norm_y_sqrd) * x
    numer_p_2 = (1 - c * norm_x_sqrd) * y
    numer = numer_p_1 + numer_p_2
    res = numer / denom
    return res


def h_scalar_mult(r: Union[float, np.float, np.array], x: np.array, c=1.0) -> np.array:
    sqrt_c = np.sqrt(c)
    factor = 1 / sqrt_c
    norm_x = np.norm(x, axis=1)
    normalized_x = x / norm_x
    inner = np.tanh(r * np.arctanh(sqrt_c * norm_x))
    res = factor * inner * normalized_x
    return res


def calculate_geodesics(x: np.array, y: np.array, t: Union[float, np.float, np.array], c=1.0) -> np.array:
    direction = h_add(-x, y, c)
    scaled_direction = h_scalar_mult(t, direction, c)
    new_position = h_add(x, scaled_direction, c)
    return new_position




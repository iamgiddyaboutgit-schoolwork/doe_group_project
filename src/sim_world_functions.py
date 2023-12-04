#!/usr/bin/env python3
"""Contains definitions of functions to be used elsewhere in the project.
"""

import numpy as np

def logistic_growth(previous_pop, r, carrying_cap):
    return round(previous_pop + r * previous_pop * (1 - previous_pop / carrying_cap))


def weight_0_more(x, b):
    """Return the y value from the equation:
    
    y = a*exp(b*x) + c
    where (x, y) = (0, 1)
    and (x, y) = (1, 0)
    are points on the curve.

    Args:
        x: float. Should be in interval [0, 1].
        b: float. positive real number

    Returns:
        float.
    """
    c = np.exp(b)/(np.exp(b) - 1)
    a = 1 - c
    y = a*np.exp(b*x) + c
    return y
#!/usr/bin/env python3
"""Contains definitions of functions to be used elsewhere in the project.
"""

import numpy as np
from scipy import stats

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

def stoch_pro_1(
    x_0, 
    max_t, 
    slope, 
    alpha, 
    sigma_errors, 
    amplitude, 
    ordinary_freq, 
    phase
):
    """Returns values of a random variable
    from a stochastic process.

    Args:
        x_0: The 0th value of the stochastic 
            process.  
        max_t: The last value of the time index
            for the process.
        slope: The approximate slope of the
            process.
        alpha: Exponential smoothing factor.
            0 < alpha < 1
        sigma_errors: Scale parameter for
            Gaussian errors.
        amplitude: Used for sinusoid term.
            Set this to 0 if a sinusoid
            term is not wanted.
        ordinary_freq: number of oscillations
            per unit time 
        phase: Used for sinusoid term.

    Returns:
        numpy.ndarray of length max_t + 1.

    For details on exponential smoothing, see:
    https://en.wikipedia.org/wiki/Exponential_smoothing

    For details on seaonality, see: 
    https://en.wikipedia.org/wiki/Sine_wave#Sine_wave_as_a_function_of_time
    """
    x = np.zeros(shape=max_t + 1)
    x[0] = x_0

    # s holds the smoothed values from the process.
    s = np.zeros(shape=max_t + 1)
    s[0] = x_0
    
    for t in range(1, max_t + 1, 1):
        # https://en.wikipedia.org/wiki/Seasonality#Modeling
        # https://en.wikipedia.org/wiki/Sine_wave#Sine_wave_as_a_function_of_time
        sinusoid = amplitude * np.sin(2*np.pi*ordinary_freq*t + phase)
        x[t] = slope + x[t - 1] + sinusoid + stats.norm(scale=sigma_errors).rvs(size=1)[0]
        s[t] = alpha * x[t] + (1 - alpha)*s[t - 1]

    return s
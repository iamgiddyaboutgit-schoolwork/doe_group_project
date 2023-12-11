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
        b: float. non-zero real number.
            Make this positive to have y 
            concave down on [0, 1].
            Make this negative to have y
            concave up on [0, 1].

    Returns:
        float.
    """
    c = np.exp(b)/(np.exp(b) - 1)
    a = 1 - c
    y = a*np.exp(b*x) + c
    return y

def stoch_pro_lin(
    x_0, 
    t_max, 
    slope, 
    alpha, 
    sigma_errors, 
    x_min=None,
    x_max=None,
    amplitude=None, 
    ordinary_freq=None, 
    phase=None
):
    """Returns a collection of random variables
    from a stochastic process.

    Args:
        x_0: The 0th value of the stochastic 
            process.  
        t_max: The last value of the time index
            for the process.
        slope: The approximate slope of the
            process.
        alpha: Exponential smoothing factor.
            0 < alpha < 1
        sigma_errors: Scale parameter for
            Gaussian errors    
        x_min: minimum value of state space
        x_max: maximum value of state space
        amplitude: Used for sinusoid term.
            Default: 0
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
    # Handle defaults
    if amplitude is None:
        amplitude = 0
    if x_min is None:
        x_min = -np.inf
    if x_max is None:
        x_max = np.inf
    if ordinary_freq is None:
        ordinary_freq = 0
    if phase is None:
        phase = 0

    x = np.zeros(shape=t_max + 1)
    x[0] = x_0

    # s holds the smoothed values from the process.
    s = np.zeros(shape=t_max + 1)
    s[0] = x_0
    
    for t in range(1, t_max + 1, 1):
        # https://en.wikipedia.org/wiki/Seasonality#Modeling
        # https://en.wikipedia.org/wiki/Sine_wave#Sine_wave_as_a_function_of_time
        sinusoid = amplitude * np.sin(2*np.pi*ordinary_freq*t + phase)
        x[t] = slope + x[t - 1] + sinusoid + stats.norm(scale=sigma_errors).rvs(size=1)[0]
        s[t] = min(x_max, max(x_min, alpha * x[t] + (1 - alpha)*s[t - 1]))

    return s

def prior_biome_before_desertification(current_biome, prob_not_desert):
    """Returns the prior biome.
    
    Args:
        current_biome: str. 
        prob_not_desert: float. This is a number between
            0 and 1 indicating the probability that the current
            desert biome used to be another biome at the start
            of the simulation.

    Returns:
        str. Indicates what the biome was historically.
    """
    ...
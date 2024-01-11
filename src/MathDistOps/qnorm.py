import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfinv

def qnorm(p, mean=0, std_dev=1, plot_graph=True):
    """
    Quantile (Inverse Cumulative Distribution Function) of the normal distribution.

    Parameters
    ----------
    - p (float): The probability for which to find the quantile.
    - mean (float, optional): The mean (average) of the normal distribution. Default is 0.
    - std_dev (float, optional): The standard deviation of the normal distribution. Default is 1.
    - plot_graph (bool, optional): Whether to plot the quantile graph. Default is True.

    Returns
    -------
    float: The value at which the cumulative probability is less than or equal to `p`.

    Formula
    -------
    Q(p; μ, σ) = μ + σ * sqrt(2) * erfinv(2p - 1)

    The quantile represents the value below which a given proportion of the distribution
    falls. It is characterized by the mean (`μ`) and standard deviation (`σ`), determining
    the center and spread of the distribution.

    Example
    -------
    >>> qnorm(0.8413447460685429, mean=0, std_dev=1)
    1.0

    Graph
    -----
    - The blue curve represents the normal distribution quantile for the given parameters.
    - The horizontal red line corresponds to the specified probability `p`.




    """
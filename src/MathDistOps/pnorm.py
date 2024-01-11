import math
import matplotlib.pyplot as plt
import numpy as np

def pnorm(x, mean=0, std_dev=1, plot_graph=True):
    """
    Cumulative Distribution Function (CDF) of the normal distribution.

    Parameters
    ----------
    x: float
        The value at which to evaluate the CDF.
    mean: float
        The mean (average) of the normal distribution. Default is 0.
    std_dev: float, optional
        The standard deviation of the normal distribution. Default is 1.
    plot_graph: bool, optional
        Whether to plot the CDF graph. Default is True.

    Returns
    -------
    float
        The cumulative probability up to the given value `x`.
    matplotlib.figure.Figure or None
        A plot of the normal distribution if 'plot_graph' is True. Otherwise, None.

    Formula
    -------
    F(x; μ, σ) = (1 / 2) * [1 + erf((x - μ) / (σ * sqrt(2)))]

    The CDF describes the probability that a random variable in a normal distribution
    is less than or equal to a specified value `x`. It is characterized by the mean (`μ`)
    and standard deviation (`σ`), determining the center and spread of the distribution.

    Example
    --------
    >>> pnorm(1, mean=0, std_dev=1)
    0.8413447460685429

    Graph
    --------
    The blue curve represents the normal distribution CDF for the given parameters.
    The vertical red line corresponds to the specified value `x`.

    Notes
    -----
    The CDF is a continuous probability distribution function, and the area under
    the curve represents the probability of the variable falling below a certain value.

    """
    pass

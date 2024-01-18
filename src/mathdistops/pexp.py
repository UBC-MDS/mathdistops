import numpy as np
import altair as alt
import pandas as pd
def qexp(p, rate, graph=False):
    """
    Calculates the cumulative probability of an exponential distribution for a given value and plots the corresponding distribution.

    This function computes the cumulative probability at a specified quantile `x` for an exponential
    distribution with a given rate parameter `lambda`. Optionally, it can generate and return a visualization
    of the distribution.

    Parameters
    ----------
    x : float
        The quantile at which to calculate the cumulative probability. Must be a non-negative number.
    rate : float
        The rate parameter (`lambda`) of the exponential distribution. Must be a positive number.
    plot_graph : bool, optional
        If True, generates and returns a plot of the exponential distribution with the cumulative probability
        highlighted for the given quantile. Default is False.

    Returns
    -------
    float
        Cumulative probability for the given quantile.
    matplotlib.figure.Figure or None
        A plot of the exponential distribution if `output_image` is True. Otherwise, None.

    Examples
    --------
    >>> pexp(0.5, rate=1, plot_graph=True)
    (0.3934693402873666, [Matplotlib Figure Object])

    Notes
    -----
    The function will raise a ValueError if `x` is negative or `rate` is non-positive.
    """
    if not 0 <= p <= 1:
        raise ValueError("Cumulative probability must be between 0 and 1.")
    if rate <= 0:
        raise ValueError("Rate parameter must be a positive number.")

    quantile = -np.log(1 - p) / rate



import numpy as np
import altair as alt
import pandas as pd
def pexp(p=0.5, rate=1, graph=True):
    """
    Calculates the quantile corresponding to given cumulative probability in an exponential distribution and plots the       corresponding distribution.

    This function computes the quantile corresponding to a specified cumulative probability `p`
    for an exponential distribution characterized by a given rate parameter `lambda`. Optionally,
    it can also generate and return a visualization of the distribution.

    Parameters
    ----------
    p : float, optional
        The cumulative probability for which to find the quantile.
        Must be between 0 and 1, exclusive of 1. Default is 0.5.
    rate : float
        The rate parameter (`lambda`) of the exponential distribution. Must be a positive number.
    graph : bool, optional
        If True, generates and returns a plot of the exponential distribution with
        the quantile highlighted for the given cumulative probability. Default is False.

    Returns
    -------
    float
        Quantile corresponding to the given cumulative probability.
    matplotlib.figure.Figure or None
        A plot of the exponential distribution if output_image is True. Otherwise, None.

    Examples
    --------
    >>> qexp(0.5, rate=1, graph=True)
    (0.6931471805599453, [Matplotlib Figure Object])

    Notes
    -----
    The function will raise a ValueError if `p` is not in the range [0, 1] or if `rate` is non-positive.
    """
    pass




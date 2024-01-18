import numpy as np
import altair as alt
import pandas as pd
def qexp(p, rate, graph=False):
    """
    Calculates the quantile corresponding to given cumulative probability in an exponential distribution and plots the corresponding distribution.

    This function computes the quantile corresponding to a specified cumulative probability `p`
    for an exponential distribution characterized by a given rate parameter `lambda`. Optionally,
    it can also generate and return a visualization of the distribution.

    Parameters
    ----------
    p : float
        The cumulative probability for which to find the quantile.
        Must be between 0 and 1, inclusive.
    rate : float
        The rate parameter (`lambda`) of the exponential distribution. Must be a positive number.
    plot_graph : bool, optional
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
    >>> qexp(0.5, rate=1, plot_graph=True)
    (0.6931471805599453, [Matplotlib Figure Object])

    Notes
    -----
    The function will raise a ValueError if `p` is not in the range [0, 1] or if `rate` is non-positive.
    """
    if not 0 <= p <= 1:
        raise ValueError("Cumulative probability must be between 0 and 1.")
    if rate <= 0:
        raise ValueError("Rate parameter must be a positive number.")

    quantile = -np.log(1 - p) / rate

    chart = None
    if graph:
        x_values = np.linspace(0, quantile * 2, 500)
        pdf_values = rate * np.exp(-rate * x_values)
        data = pd.DataFrame({'x': x_values, 'PDF': pdf_values})

        line = alt.Chart(data).mark_line().encode(
            x='x',
            y='PDF'
        )
        point = alt.Chart(pd.DataFrame({'x': [quantile], 'PDF': [rate * np.exp(-rate * quantile)]})).mark_point(color='red').encode(
            x='x',
            y='PDF'
        )

        chart = alt.layer(line, point).properties(
            title='Exponential Distribution (PDF)',
            width=600,
            height=400
        )
        
    return quantile, chart
    
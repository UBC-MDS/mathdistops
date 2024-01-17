from scipy.special import erf
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import altair as alt
import pandas as pd

def pexp(q=None, rate=1, graph=True):
    """
    Calculates the cumulative probability of the exponential distribution at this quantile and plots corresponding PDF and CDF.

    This function computes the cumulative probability at a specified quantile `x` for an exponential
    distribution with a given rate parameter `lambda`. Optionally, it can generate and return a visualization
    corresponding PDF and CDF.

    Parameters
    ----------
    q : float
        The quantile at which to evaluate the CDF. Default is None.
    rate : float
        The rate parameter (lambda) of the exponential distribution. Default is 1.
    graph : bool
        Whether to plot the PDF and CDF graph. Default is True.

    Returns
    -------
    result : pandas.DataFrame or tuple
        If `graph` is True (default), returns a tuple consisting of a pandas DataFrame and a 
            layered altair Chart consisting of two graphs, CDF and PDF.
        If `graph` is False, returns a pandas DataFrame.

    Examples
    --------
    >>> pexp(0.5, rate=1, plot_graph=True)
    (0.3934693402873666, [Matplotlib Figure Object])

    Notes
    -----
    The function will raise a ValueError if `x` is negative or `rate` is non-positive.
    """
    # Calculate cumulative probability
    prob = 1 - math.exp(-rate * q)
    results_df = pd.DataFrame({'Quantile': [q], 'Cumulative probability': [prob]})

    x_values = np.linspace(0, q + 3 / rate, 1000)
    y_values_pdf = rate * np.exp(-rate * x_values)
    y_values_cdf = 1 - np.exp(-rate * x_values)
    data = {'x': x_values, 'pdf': y_values_pdf, 'cdf': y_values_cdf, 'q': q}
    df = pd.DataFrame(data)
    
    # PDF
    chart = alt.Chart(df).mark_line().encode(
        x='x',
        y='pdf'
    )

    #Add a shaded area under the curve ()
    shade_area = alt.Chart(df, title=f'Probability Density Function for q = {q}, rate = {rate}').mark_area(opacity=0.3, color='lightblue').encode(
        x=alt.X('x', title='X'),
        y=alt.Y('pdf', title='f(X)')
    ).transform_filter(
        alt.datum.x <= q  
    )

    # Add vertical line at respective quantile 
    vertline = alt.Chart(pd.DataFrame({'q': [q]})).mark_rule(strokeDash=[3, 3]).encode(
        x='q'
    )

    # CDF
    cdf_chart = alt.Chart(df, title=f'Cumulative Distribution Function for q = {q}, rate = {rate}').mark_line().encode(
        x=alt.X('x').title("x"),
        y=alt.Y('cdf').title('probability'),
        color=alt.value('orange'),
        opacity=alt.value(0.5),
    ).properties(
        width=300,
        height=150
    )

    # Combine all plots
    result_graph = (shade_area + chart + vertline) |(cdf_chart + vertline)

    if graph == True: 
        return results_df, result_graph
    else:
        return results_df
import math
import numpy as np
import altair as alt
import pandas as pd

def pexp(q, rate=1, graph=True):
    """
    Calculates the cumulative probability of the exponential distribution at this quantile and plots corresponding PDF and CDF.

    This function computes the cumulative probability at a specified quantile `q` for an exponential
    distribution with a given rate parameter `lambda`. Optionally, it can generate and return a visualization
    corresponding PDF and CDF.

    Parameters
    ----------
    q : float
        The quantile at which to evaluate the CDF.
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
    >>> pexp(0.5, rate=1, graph=False)
        Quantile    Cumulative probability
    0   0.5         0.393469
    """

    if rate <= 0:
        raise ValueError("Rate cannot be zero or negative.")

    if not isinstance(q, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("Input parameters must be numerical.")
    
    if q < 0:
        raise ValueError("Quantile 'q' should not be below zero")
        
    # Calculate cumulative probability

    prob = 1 - math.exp(-rate * q)
    results_df = pd.DataFrame({'Quantile': [q], 'Cumulative probability': [prob]})

    if graph:
        x_values = np.linspace(0, q + 3 / rate, 1000)
        y_values_pdf = rate * np.exp(-rate * x_values)
        y_values_cdf = 1 - np.exp(-rate * x_values)
        data = {'x': x_values, 'pdf': y_values_pdf, 'cdf': y_values_cdf, 'q': q}
        df = pd.DataFrame(data)
        
        # PDF
        chart = alt.Chart(
            df,
            title=alt.Title(
            text='Probability Density Function',
            subtitle=f'for q = {q:.4g}, rate = {rate:.4g}')
        ).mark_line().encode(
            x='x',
            y='pdf'
        ).properties(
            width=250,
            height=250
        )

        #Add a shaded area under the curve ()
        shade_area = alt.Chart(df).mark_area(opacity=0.3, color='lightblue').encode(
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
        cdf_chart = alt.Chart(
            df,
            title=alt.Title(
            text='Cumulative Distribution Function',
            subtitle=f'for q = {q:.4g}, rate = {rate:.4g}')
        ).mark_line().encode(
            x=alt.X('x').title("x"),
            y=alt.Y('cdf').title('probability'),
            color=alt.value('orange'),
            opacity=alt.value(0.5),
        ).properties(
            width=250,
            height=250
        )

        horizontalline = alt.Chart(pd.DataFrame({'p': [prob]})).mark_rule(strokeDash=[3, 3]).encode(
            y='p'
        )

        # Combine all plots
        result_graph = (shade_area + chart + vertline) |(cdf_chart + vertline + horizontalline)

        return results_df, result_graph

    return results_df
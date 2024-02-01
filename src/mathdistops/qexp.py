import numpy as np
import altair as alt
import pandas as pd

def qexp(p, rate=1, graph=True):

    """
    Calculates the quantile corresponding to given cumulative probability in an exponential distribution and plots the corresponding distribution.

    This function computes the quantile corresponding to a specified cumulative probability `p`
    for an exponential distribution characterized by a given rate parameter `lambda`. Optionally,
    it can also generate and return a visualization of the distribution.

    Parameters
    ----------
    p : float, optional
        The cumulative probability for which to find the quantile.
        Must be between 0 and 1, exclusive of 1. 
    rate : float
        The rate parameter (`lambda`) of the exponential distribution. Must be a positive number. Default is 1
    graph : bool, optional
        If True, generates and returns a plot of the exponential distribution with
        the quantile highlighted for the given cumulative probability. Default is True.

    Returns
    -------
    result : pandas.DataFrame or tuple
        If `graph` is True (default), returns a tuple consisting of a pandas DataFrame giving you the 
        cumulative probability and the quantile as well as a layered altair Chart consisting of two graphs, CDF and PDF.
        If `graph` is False, returns a pandas DataFrame.

    Examples
    --------
    >>> qexp(0.5, rate=1, graph=False)
        Probability     Quantile
    0   0.5             0.6931471805599453
    """
    if not 0 <= p < 1:
        raise ValueError("Cumulative probability must be between 0 and 1, exclusive of 1")
    if rate <= 0:
        raise ValueError("Rate parameter must be a positive number.")
    quantile = -np.log(1 - p) / rate
    results_df = pd.DataFrame({'Probability': [p], 'Quantile': [quantile]})

    
    if graph:
        x_values = np.linspace(0, quantile + 3 / rate, 1000)
        pdf_values = rate * np.exp(-rate * x_values)
        cdf_values = 1 - np.exp(-rate * x_values)
        data = pd.DataFrame({'x': x_values, 'PDF': pdf_values, 'CDF': cdf_values, 'q': quantile})

        # PDF plot
        pdf_chart = alt.Chart(
            data,
            title=alt.Title(
                text='Probability Density Function',
                subtitle=f'for p = {p:.4g}, rate = {rate:.4g}'
            )
        ).mark_line().encode(
            x='x',
            y='PDF'
        ).properties(
            width=250,
            height=250
        )
        vertline = alt.Chart(pd.DataFrame({'x': [quantile]})).mark_rule(strokeDash=[3, 3]).encode(
            x='x',
            color=alt.value('red')
        )
        shade_area = alt.Chart(data).mark_area(opacity=0.3, color='lightblue').encode(
            x=alt.X('x', title='X'),
            y=alt.Y('PDF', title='f(X)')
        ).transform_filter(
            alt.datum.x <= quantile
        )

        cdf_chart = alt.Chart(
            data,
            title=alt.Title(
                text='Cumulative Distribution Function',
                subtitle=f'for p = {p:.4g}, rate = {rate:.4g}'
            )
        ).mark_line().encode(
            x=alt.X('x').title("x"),
            y=alt.Y('CDF').title('probability'),
            color=alt.value('orange'),
            opacity=alt.value(0.5),
        ).properties(
            width=250,
            height=250
        )
      
        vertline = alt.Chart(pd.DataFrame({'q': [quantile]})).mark_rule(strokeDash=[3, 3]).encode(
        x='q'
        )

        horizontalline = alt.Chart(pd.DataFrame({'p': [p]})).mark_rule(strokeDash=[3, 3]).encode(
        y='p'
        )
        chart = (pdf_chart + vertline + shade_area) | (cdf_chart + vertline +horizontalline)

        return results_df, chart
    
    return results_df


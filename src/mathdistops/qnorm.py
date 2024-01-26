import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfinv
import scipy.stats as stats
import math
import altair as alt
import pandas as pd

def qnorm(p, mean=0, std_dev=1, graph=True):
    """
    Quantile (Inverse Cumulative Distribution Function) of the normal distribution.

    Parameters
    ----------
    p: float
        The probability for which to find the quantile.
    mean: float, optional
        The mean (average) of the normal distribution. Default is 0.
    std_dev: float, optional
        The standard deviation of the normal distribution. Default is 1.
    graph: bool, optional
        Whether to plot the PDF and CDF graphs. Default is True.

    Returns
    -------
    result : pandas.DataFrame or tuple
        If `graph` is True (default), returns a tuple consisting a pandas DataFrame and a 
            layered altair Chart consisting of two graphs, CDF and PDF
        If `graph` is False, returns a pandas DataFrame..

    Example
    -------
    >>> qnorm(0.8413447460685429, mean=0, std_dev=1)
    1.0

    """
    
    if p is None:
        raise ValueError("Parameter 'p' is required.")

    if not all(isinstance(param, (int, float)) for param in [p, mean, std_dev]):
        raise TypeError("Input parameters must be numerical.")

    if p<0 or p>1:
        raise ValueError("Parameter 'p' stands for probability, which should have a value between 0 and 1 only.")

    if std_dev <= 0:
        raise ValueError("Standard deviation cannot be zero or negative.")

    #Calculate quantile
    q = mean + std_dev * math.sqrt(2) * erfinv(2*p - 1)

    # Standardizing the names
    x = q 
    z = (x - mean) / std_dev
    prob = p
    
    results_df = pd.DataFrame({'Quantile': [q]})
    
    x_values = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 100)
    y_values_pdf = stats.norm.pdf(x_values, mean, std_dev)
    y_values_cdf = stats.norm.cdf(x_values, mean, std_dev)
    data = {'x': x_values, 'pdf': y_values_pdf, 'cdf': y_values_cdf, 'q': q}
    df = pd.DataFrame(data)
    
    # PDF
    chart = alt.Chart(df).mark_line().encode(
        x='x',
        y='pdf'
    )
    
    #Add a shaded area under the curve ()
    shade_area = alt.Chart(df, title=f"Probability Density Function for p = {prob:.4g}, mean = {mean:.4g}, sd = {std_dev:.4g}").mark_area(opacity=0.3, color='lightblue').encode(
        x=alt.X('x', title='X'),
        y=alt.Y('pdf', title='f(X)')
    ).transform_filter(
        alt.datum.x <= x  
    )
    
    # Add vertical line at respective quantile 
    vertline = alt.Chart(pd.DataFrame({'z': [q]})).mark_rule(strokeDash=[3, 3]).encode(
        x='z'
    )
    #CDF
    cdf_chart = alt.Chart(df, title=f"Cumulative Distribution Chart for p = {prob:.4g}, mean = {mean:.4g}, sd = {std_dev:.4g}").mark_line().encode(
        x=alt.X('x').title("x"),
        y=alt.Y('cdf').title('probability'),
        color=alt.value('orange'),
        opacity=alt.value(0.5),
    ).properties(
        width=300,
        height=300
    )

    horizontalline = alt.Chart(pd.DataFrame({'p': [prob]})).mark_rule(strokeDash=[3, 3]).encode(
        y='p'
    )
    
    # Combine all plots
    result_graph = (shade_area + chart + vertline) |(cdf_chart + vertline + horizontalline)

    if graph == True: 
        return results_df, result_graph
    else:
        return results_df
    
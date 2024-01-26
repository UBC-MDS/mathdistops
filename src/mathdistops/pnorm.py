from scipy.special import erf
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import altair as alt
import pandas as pd

def pnorm(q, mean = 0, std_dev =1, graph = True):
    """
    Calculates Cumulative Probability of the normal distribution at this quantile and plots corresponding PDF and CDF.

    Parameters
    ----------
    q: float
        The quantile at which to evaluate the CDF.
    mean: float
        The mean (average) of the normal distribution. Default is 0.
    std_dev: float
        The standard deviation of the normal distribution. Default is 1.
    graph: bool
        Whether to plot the PDF and CDF graph. Default is True.

    Returns
    -------
    result : pandas.DataFrame or tuple
        If `graph` is True (default), returns a tuple consisting a pandas DataFrame and a 
            layered altair Chart consisting of two graphs, CDF and PDF
        If `graph` is False, returns a pandas DataFrame.

    Example
    --------
    >>> pnorm(1, mean=0, std_dev=1)
    0.8413447460685429

    """
    if q is None:
        raise ValueError("Parameter 'q' is required.")

    if std_dev <= 0:
        raise ValueError("Standard deviation cannot be zero or negative.")

    if not all(isinstance(param, (int, float)) for param in [q, mean, std_dev]):
        raise TypeError("Input parameters must be numerical.")

    #Calculate z-score and cumulative probability
    x = q 
    z = (x - mean) / std_dev
    prob = 1/2 * (1 + erf(z / math.sqrt(2)))
    
    results_df = pd.DataFrame({'Z-score': [z], 'Cumulative probability': [prob]})
    
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
    shade_area = alt.Chart(df, title=f"Probability Density Function for q = {q:.4g}, mean = {mean:.4g}, sd = {std_dev:.4g}").mark_area(opacity=0.3, color='lightblue').encode(
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
    cdf_chart = alt.Chart(df, title=f"Cumulative Distribution Chart for q = {q:.4g}, mean = {mean:.4g}, sd = {std_dev:.4g}").mark_line().encode(
        x=alt.X('x').title("x"),
        y=alt.Y('cdf').title('probability'),
        color=alt.value('orange'),
        opacity=alt.value(0.5),
    ).properties(
        width=300,
        height=300
    )

    # Add horiozontal line at respective p
    horizontalline = alt.Chart(pd.DataFrame({'p': [prob]})).mark_rule(strokeDash=[3, 3]).encode(
        y='p'
    )
    
    # Combine all plots
    result_graph = (shade_area + chart + vertline) |(cdf_chart + vertline + horizontalline)

    if graph == True: 
        return results_df, result_graph
    else:
        return results_df

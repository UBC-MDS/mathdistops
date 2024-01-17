def pexp(x, rate, plot_graph=False):
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


    if graph:
        return pdf_chart
    else:
        return results_df
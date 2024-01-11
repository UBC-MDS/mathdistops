def pexp(x, rate, output_image=False):
    """
    Calculates the exponential distribution cumulative probability for a given value and plots the corresponding distribution

    Parameters:
    - x (float): The quantile at which to calculate the cumulative probability.
    - rate (float): The rate parameter (lambda) of the exponential distribution.
    - output_image (bool, optional): If True, generates and returns a plot of the exponential 
      distribution with the cumulative probability highlighted for the given quantile. Default is False.

    Returns:
    - float: Cumulative probability for the given quantile.
    - matplotlib.figure.Figure (optional): A plot of the exponential distribution if output_image is True.

    Example:
    >>> pexp(0.5, rate=1, output_image=True)
    (0.3934693402873666, <Figure ...>)
    """
    pass  # To be implemented

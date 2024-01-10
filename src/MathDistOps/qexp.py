def qexp(p, rate, output_image=False):
    """
    Calculates the quantile corresponding to given cumulative probability in an exponential distribution.

    Parameters:
    - p (float): The cumulative probability for which to find the quantile.
    - rate (float): The rate parameter (lambda) of the exponential distribution.
    - output_image (bool, optional): If True, generates and returns a plot of the exponential 
      distribution with the quantile highlighted for the given cumulative probability. Default is False.

    Returns:
    - float: Quantile corresponding to the given cumulative probability.
    - matplotlib.figure.Figure (optional): A plot of the exponential distribution if output_image is True.

    Example:
    >>> qexp(0.5, rate=1, output_image=True)
    (0.6931471805599453, <Figure ...>)
    """
    pass  # To be implemented

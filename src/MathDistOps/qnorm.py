import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfinv

def qnorm(p, mean=0, std_dev=1, plot_graph=True):
    """
    Quantile (Inverse Cumulative Distribution Function) of the normal distribution.

    Parameters
    ----------
    - p (float): The probability for which to find the quantile.
    - mean (float, optional): The mean (average) of the normal distribution. Default is 0.
    - std_dev (float, optional): The standard deviation of the normal distribution. Default is 1.
    - plot_graph (bool, optional): Whether to plot the quantile graph. Default is True.



    """
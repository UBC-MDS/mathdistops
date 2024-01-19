from mathdistops.qexp import qexp
import pytest
import altair as alt
import numpy as np
import pandas as pd

def test_quantile_calculation():
    """
    Tests whether function calculates quantile correctly.
    """
    # Known values for specific cases
    assert qexp(0.5, 1, False)['Quantile'].iloc[0]== -np.log(0.5)
    assert qexp(0.75, 2, False)['Quantile'].iloc[0]== -np.log(0.25) / 2


def test_output_datatypes():
    """
    Tests whether function returns correct output data types.
    """
    df, chart = qexp(0.5, 1, graph=True)
    assert isinstance(df, pd.DataFrame)
    assert hasattr(chart, 'hconcat')
    assert len(chart.hconcat) == 2


def test_invalid_probability_input():
    """
    Tests function's response to invalid probability values, including the edge case of p=1 and p=None.
    """
    with pytest.raises(ValueError) as custom_string:
        results = qexp(None)
    assert str(custom_string.value) == "Parameter 'p' is required."
    
    with pytest.raises(ValueError) as excinfo:
        qexp(-0.1, 1)
    assert str(excinfo.value) == "Cumulative probability must be between 0 and 1, exclusive of 1"

    with pytest.raises(ValueError) as excinfo:
        qexp(1.1, 1)
    assert str(excinfo.value) == "Cumulative probability must be between 0 and 1, exclusive of 1"

    with pytest.raises(ValueError) as excinfo:
        qexp(1, 1)
    assert str(excinfo.value) == "Cumulative probability must be between 0 and 1, exclusive of 1"

    
def test_missing_input():
    """
    Test case for TypeError when parameter `p` is missing.
    """
    with pytest.raises(TypeError) as custom_string:
        results, graph = qexp()
    assert str(custom_string.value) ==  "qexp() missing 1 required positional argument: 'p'"

def test_invalid_rate_input():
    """
    Tests function's response to invalid rate values.
    """
    with pytest.raises(ValueError) as excinfo:
        qexp(0.5, 0)
    assert str(excinfo.value) == "Rate parameter must be a positive number."

    with pytest.raises(ValueError) as excinfo:
        qexp(0.5, -1)
    assert str(excinfo.value) == "Rate parameter must be a positive number."

def test_graph_properties():
    """
    Tests if the plot has the correct properties.
    """
    _, chart = qexp(0.5, 1, graph=True)
    assert hasattr(chart, 'hconcat')
    assert len(chart.hconcat) == 2


from mathdistops.qexp import qexp
import pytest
import altair as alt
import numpy as np

def test_quantile_calculation():
    """
    Tests whether function calculates quantile correctly.
    """
    # Known values for specific cases
    assert qexp(0.5, 1, False)[0] == -np.log(0.5)
    assert qexp(0.75, 2, False)[0] == -np.log(0.25) / 2

def test_output_datatypes():
    """
    Tests whether function returns correct output data types.
    """
    quantile, graph = qexp(0.5, 1, graph=True)
    assert isinstance(quantile, float)
    assert isinstance(graph, alt.LayerChart) or graph is None

def test_invalid_probability_input():
    """
    Tests function's response to invalid probability values.
    """
    with pytest.raises(ValueError) as excinfo:
        qexp(-0.1, 1)
    assert str(excinfo.value) == "Cumulative probability must be between 0 and 1."

    with pytest.raises(ValueError) as excinfo:
        qexp(1.1, 1)
    assert str(excinfo.value) == "Cumulative probability must be between 0 and 1."

def test_invalid_rate_input():
    """
    Tests function's response to invalid rate values.
    """
    with pytest.raises(ValueError) as excinfo:
        qexp(0.5, 0)
    assert str(excinfo.value) == "Rate parameter must be a positive number."
    
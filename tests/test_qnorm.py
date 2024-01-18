from mathdistops.qnorm import qnorm
import pytest
import pandas as pd
import altair as alt

def test_output_datatype():
    """
    Tests whether function returns correct output data objects.
    """
    results, graph = qnorm(0.7, mean=2, std_dev=3)
    assert isinstance(results, pd.DataFrame)
    assert hasattr(graph, 'hconcat')
    assert len(graph.hconcat) == 2

def test_df_results():
    """
    Tests whether function calculates quantile value correctly.
    """
    results = qnorm(0.5, graph=False)
    assert results.shape == (1, 1)
    assert results['Quantile'].iloc[0] == 0

    results_df = qnorm(0.25, graph=False)
    assert abs(results_df['Quantile'].iloc[0] - (-0.67449)) <= 0.001

def test_missing_input():
    """
    Test case for TypeError when parameter `p` is missing.
    """
    with pytest.raises(TypeError) as custom_string:
        results, graph = qnorm()
    assert str(custom_string.value) ==  "qnorm() missing 1 required positional argument: 'p'"


def test_p_outofrange():
    """
    Test case for ValueError when parameter `p` is out of range.
    """
    with pytest.raises(ValueError) as custom_string:
        results, graph = qnorm(5)
    assert str(custom_string.value) == "Parameter 'p' stands for probability, which should have a value between 0 and 1 only."
    

def test_nonsensical_input():
    """
    Test case for ValueError and Type Error in case of incorrect user input, e.g. negative standard deviation or non numerical value.
    """
    with pytest.raises(ValueError) as custom_string:
        results = qnorm(0.3, mean=5, std_dev=-2, graph=False)
    assert str(custom_string.value) == "Standard deviation cannot be zero or negative."

    with pytest.raises(TypeError) as custom_string:
        results = qnorm('hi', mean=5, std_dev=2, graph=False)
    assert str(custom_string.value), "Input parameters must be numerical."

    with pytest.raises(ValueError) as custom_string:
        results = qnorm(None)
    assert str(custom_string.value), "Parameter 'p' is required."





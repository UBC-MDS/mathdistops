from mathdistops.pnorm import pnorm
import pytest
import pandas as pd
import altair as alt

def test_output_datatype():
    """
    Tests whether function returns correct output data types 
    """
    results, graph = pnorm(1.5, mean=2, std_dev=3)
    assert isinstance(results, pd.DataFrame)
    assert hasattr(graph, 'hconcat')
    assert len(graph.hconcat) == 2

def test_df_results():
    """
    Tests whether function calculates z-score and probability value correctly
    """
    results = pnorm(0, graph=False)
    assert results.shape == (1, 2)
    assert results['Z-score'].iloc[0] == 0
    assert results['Cumulative probability'].iloc[0] == 0.5

    results_df = pnorm(2, graph=False)
    assert results_df['Z-score'].iloc[0] == 2
    cumulative_probability = results_df['Cumulative probability'].iloc[0]
    assert 0 <= cumulative_probability <= 1


def test_nonsensical_input():
    """
    Test case for ValueError and Type Error in case of incorrect user input, e.g. negative standard deviation or non numerical value
    """
    with pytest.raises(ValueError) as custom_string:
        results = pnorm(3, mean=5, std_dev=-2, graph=False)
    assert str(custom_string.value) == "Standard deviation cannot be zero or negative."

    with pytest.raises(TypeError) as custom_string:
        results = pnorm('hi', mean=5, std_dev=2, graph=False)
    assert str(custom_string.value) == "Input parameters must be numerical."

    with pytest.raises(ValueError) as custom_string:
        results = pnorm(None)
    assert str(custom_string.value) == "Parameter 'q' is required."


    


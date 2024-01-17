from mathdistops.pnorm import pnorm
import pytest
import pandas as pd
import altair as alt

def test_output_datatype_pexp():
    """
    Tests whether the pexp function returns correct output data types 
    """
    results, graph = pexp(1.5, rate=1)
    assert isinstance(results, pd.DataFrame), "Expected DataFrame output for results"
    assert hasattr(graph, 'hconcat'), "Expected concatenated altair Chart for graph"
    assert len(graph.hconcat) == 2, "Expected two concatenated charts"

def test_df_results_pexp():
    """
    Tests whether the pexp function calculates the cumulative probability value correctly
    """
    results = pexp(1, graph=False)
    assert results.shape == (1, 2), "Expected DataFrame shape to be (1, 2)"
    assert results['Quantile'].iloc[0] == 1, "Expected correct quantile value"
    assert 0 <= results['Cumulative probability'].iloc[0] <= 1, "Expected cumulative probability to be between 0 and 1"

    results_df = pexp(2, rate=2, graph=False)
    assert results_df['Quantile'].iloc[0] == 2, "Expected correct quantile value"
    cumulative_probability = results_df['Cumulative probability'].iloc[0]
    assert 0 <= cumulative_probability <= 1, "Expected cumulative probability to be between 0 and 1"



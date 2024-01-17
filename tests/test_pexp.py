from mathdistops.pnorm import pnorm
import pytest
import pandas as pd
import altair as alt

def test_output_datatype():
    """
    Tests whether the pexp function returns correct output data types 
    """
    results, graph = pexp(1.5, rate=1)
    assert isinstance(results, pd.DataFrame), "Expected DataFrame output for results"
    assert hasattr(graph, 'hconcat'), "Expected concatenated altair Chart for graph"
    assert len(graph.hconcat) == 2, "Expected two concatenated charts"


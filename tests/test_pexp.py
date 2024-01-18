from mathdistops.pexp import pexp
import pytest
import pandas as pd
import altair as alt
import math

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
    results = pexp(1, rate=1, graph=False)
    expected_probability = 1 - math.exp(-1)
    assert results.shape == (1, 2), "Expected DataFrame shape to be (1, 2)"
    assert results['Quantile'].iloc[0] == 1, "Expected correct quantile value"
    assert results['Cumulative probability'].iloc[0] == pytest.approx(expected_probability), "Expected cumulative probability did not match for q=1, rate=1"

    results_df = pexp(2, rate=2, graph=False)
    expected_probability_df = 1 - math.exp(-2 * 2)
    assert results_df['Quantile'].iloc[0] == 2, "Expected correct quantile value"
    assert results_df['Cumulative probability'].iloc[0] == pytest.approx(expected_probability_df), "Expected cumulative probability did not match for q=2, rate=2"

def test_missing_input_pexp():
    """
    Test case for ValueError when parameter `q` is missing in pexp.
    """
    with pytest.raises(ValueError) as custom_string:
        results, graph = pexp()
    assert str(custom_string.value) == "Parameter 'q' is required.", "Expected a ValueError for missing 'q' parameter"

def test_nonsensical_input_pexp():
    """
    Test case for ValueError and TypeError in case of incorrect user input for pexp, e.g. negative rate or non-numerical value.
    """
    with pytest.raises(ValueError) as custom_string:
        results = pexp(3, rate=-1, graph=False)
    assert str(custom_string.value) == "Rate cannot be zero or negative."

    with pytest.raises(TypeError) as custom_string:
        results = pexp('hi', rate=2, graph=False)
    assert str(custom_string.value), "Input parameters must be numerical."

def test_figure_components_pexp():
    """
    Tests whether the pexp function creates figures with the correct components.
    """
    _, graph = pexp(1.5, rate=1)
    assert isinstance(graph, (alt.Chart, alt.LayerChart, alt.HConcatChart)), "Expected graph to be an Altair Chart, LayerChart, or HConcatChart object"
    graph_dict = graph.to_dict()

    pdf_found = False
    cdf_found = False
    rule_found = False
    area_found = False

    if isinstance(graph, alt.HConcatChart):
        charts = graph_dict['hconcat']
    else:
        charts = [graph_dict]

    for chart_dict in charts:
        layers = chart_dict.get('layer', [])
        for layer in layers:
            mark_type = layer.get('mark', {}).get('type', '')
            encoding = layer.get('encoding', {})
            y_field = encoding.get('y', {}).get('field', '')

            if mark_type == 'line' and y_field == 'pdf':
                pdf_found = True

            if mark_type == 'line' and y_field == 'cdf':
                cdf_found = True

            if mark_type == 'rule':
                rule_found = True

            if mark_type == 'area' and y_field == 'pdf':
                area_found = True

    assert pdf_found, "Expected PDF line in charts"
    assert cdf_found, "Expected CDF line in charts"
    assert rule_found, "Expected vertical line at quantile in charts"
    assert area_found, "Expected shaded area under the PDF curve in charts"


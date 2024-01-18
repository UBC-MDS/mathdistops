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

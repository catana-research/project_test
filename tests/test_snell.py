# example/tests/test_examples.py
import numpy as np
import pytest
from project_test.snell import snell


@pytest.mark.parametrize('n1, n2', [(2.00, 3.00), (3.00, 2.00),])
def test_perpendicular(n1, n2):
    # For any indexes, a ray normal to the surface should not bend.
    # We'll try a couple different combinations of indexes....

    actual = snell(0, n1, n2)
    expected = 0
    assert actual == expected


def test_air_water():
    n_air, n_water = 1.00, 1.33
    actual = snell(np.pi/4, n_air, n_water)
    expected = 0.5605584137424605
    assert np.allclose(actual, expected)

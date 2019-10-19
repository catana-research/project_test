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

# Fixtures are used to setup test data that is used frequently
@pytest.fixture
def peak():
    # Construct a 1-dimensional Gaussian peak.
    x = np.linspace(-10, 10, num=21)
    sigma = 3.0
    peak = np.exp(-(x / sigma)**2 / 2) / (sigma * np.sqrt(2 * np.pi))
    return peak


def test_gaussian_mean(peak):
    actual = np.mean(peak)
    expected = 0.04759819937913877
    assert np.allclose(actual, expected)


def test_gaussian_std(peak):
    actual = np.std(peak)
    expected = 0.04703300841553288
    assert np.allclose(actual, expected)


def test_gaussian_positive(peak):
    # Test that there are no negative values.
    assert np.all(peak >= 0)

import pytest
from   project_test.project_test import Cat

"""Tests for `project_test` package."""


@pytest.fixture
def load_cat():
    cat = Cat()
    return cat


def test_meow_basic(load_cat):
    """Demonstrate use of fixtures

    Fixtures enable test data to be prepared and shared between tests
    """
    cat = load_cat

    if not cat:
        pytest.fail("Cat is not configured")
    assert cat.meow(10, 1) == 'Meow', 'Cat Meow is of incorrect format'


@pytest.mark.parametrize("test_input, expected", [((10, 1, None), 'Meow'),  # Normal Meow
                                                  ((100, 1, None), 'MEOW'),  # Loud Meow
                                                  ((10, 1, 'cute'), 'Meow ^_^'),  # Cute Meow
                                                  ((100, 1, 'cute'), 'MEOW ^_^'),  # Cute loud Meow
                                                  ((10, 5, None), 'Meooooow'),  # Long Meow
                                                  ])
def test_meow(test_input, expected):
    """ Parameterized test method for cat """
    cat = Cat()
    print(*test_input)
    assert cat.meow(*test_input) == expected, 'Cat Meow is of incorrect format'


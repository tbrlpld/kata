# -*- coding: utf-8 -*-

"""Tests for the change program."""

import pytest
#
from change import ChangeMaker


@pytest.mark.parametrize(
    (
        "cents",
        "expected_change",
    ),
    (
        (1, {"pennies": 1}),
        (3, {"pennies": 3}),
        (5, {"nickels": 1}),
        (6, {"nickels": 1, "pennies": 1}),
        (11, {"dimes": 1, "pennies": 1}),
        (15, {"dimes": 1, "nickels": 1}),
        (26, {"quarters": 1, "pennies": 1}),
        (41, {"quarters": 1, "dimes": 1, "nickels": 1, "pennies": 1}),
        (51, {"quarters": 2, "pennies": 1}),
    ),
)
def test_change(cents, expected_change):
    """
    Test the main functionality of the program.

    This is basically a black box test and does not care about the internal
    workings. It only defined the input integer and the expected result, which
    is a dictionary with they coin names as the keys and the number of these
    coins as the value. Coins that are not used to generate the change are
    also not included in the dictionary.
    """
    changemaker = ChangeMaker()
    returned_change = changemaker.get_change(cents)
    assert isinstance(returned_change, dict)
    assert returned_change.get("quarters") == expected_change.get("quarters")
    assert returned_change.get("dimes") == expected_change.get("dimes")
    assert returned_change.get("nickels") == expected_change.get("nickels")
    assert returned_change.get("pennies") == expected_change.get("pennies")

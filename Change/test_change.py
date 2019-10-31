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
        (1, {"penny": 1}),
        (3, {"penny": 3}),
        (5, {"nickel": 1}),
        (6, {"nickel": 1, "penny": 1}),
        (11, {"dime": 1, "penny": 1}),
        (15, {"dime": 1, "nickel": 1}),
        (26, {"quarter": 1, "penny": 1}),
        (41, {"quarter": 1, "dime": 1, "nickel": 1, "penny": 1}),
        (51, {"quarter": 2, "penny": 1}),
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
    assert returned_change.get("quarter") == expected_change.get("quarter")
    assert returned_change.get("dime") == expected_change.get("dime")
    assert returned_change.get("nickel") == expected_change.get("nickel")
    assert returned_change.get("penny") == expected_change.get("penny")

# -*- coding: utf-8 -*-

"""Tests for the change program."""

import pytest
#
from change import change


@pytest.mark.parametrize(
    ("cents", "expected_change"),
    (
        (1, {"penny": 1}),
        (3, {"penny": 3}),
        (5, {"nickel": 1}),
        (6, {"nickel": 1, "penny": 1}),
        (11, {"dime": 1, "penny": 1}),
        (15, {"dime": 1, "nickel": 1}),
    ),
)
def test_change(cents, expected_change):
    """Test change function."""
    returned_change = change(cents)
    assert returned_change.get("quarter") == expected_change.get("quarter")
    assert returned_change.get("dime") == expected_change.get("dime")
    assert returned_change.get("nickel") == expected_change.get("nickel")
    assert returned_change.get("penny") == expected_change.get("penny")

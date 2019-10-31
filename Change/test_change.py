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
        (5, {"nickle": 1}),
        (6, {"nickle": 1, "penny": 1}),
    ),
)
def test_change(cents, expected_change):
    """Test change function."""
    returned_change = change(cents=1)
    assert returned_change.get("penny") == expected_change.get("penny")
    assert returned_change.get("nickle") == expected_change.get("nickle")
    assert returned_change.get("dime") == expected_change.get("dime")
    assert returned_change.get("quarter") == expected_change.get("quarter")


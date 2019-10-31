# -*- coding: utf-8 -*-

"""Tests for the change program."""

from change import change


def test_change():
    """Test change function."""
    returned_change = change(cents=1)
    assert returned_change["penny"] == 1

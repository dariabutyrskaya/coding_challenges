"""
Tests
"""
import pytest
from main import subseq


def test_one():
    assert subseq([10,9,2,5,3,7,101,18]) == 4, "Should be 4"


def test_two():
    assert subseq([7,7,7,7,7,7,7]) == 1, "Should be 1"


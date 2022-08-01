"""
This script contains the tests
"""
import pytest
from main import findmin


def test_one():
    assert findmin([3,4,5,1,2]) == 1, "Should be 1"


def test_two():
    assert findmin([4,5,6,7,0,1,2]) == 0, "Should be 0"


def test_three():
     assert findmin([11,13,15,17]) == 11, "Should be 11"


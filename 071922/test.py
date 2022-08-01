"""
Tests
"""
import pytest
from main import longest_no_repeat


def test_one():
    assert longestnorepeat("abcabcbb") == 3, "Should be 3"


def test_two():
    assert longestnorepeat("bbbbb") == 1, "Should be 1"


def test_three():
     assert longestnorepeat("pwwkew") == 3, "Should be 3"

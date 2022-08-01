"""
Tests
"""
import pytest
from main import characterReplacement


def test_one():
    assert characterReplacement("ABAB", 2) == 4, "Should be 4"


def test_two():
    assert characterReplacement("AABABBA", 1) == 1, "Should be 1"


import pytest
from main import topKFrequent


def test_1():
    assert topKFrequent([1,1,1,2,2,3], 2) == [1,2], "Should be [1,2]"


def test_2():
    assert topKFrequent([1], 1) == [1], "Should be [1]"


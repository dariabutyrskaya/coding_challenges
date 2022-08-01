
import pytest
from main import merge


def test_1():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]], "Should be [[1,6],[8,10],[15,18]]"


def test_2():
    assert merge([[1,4],[4,5]]) == [[1,4],[4,5]], "Should be [[1,4],[4,5]]"



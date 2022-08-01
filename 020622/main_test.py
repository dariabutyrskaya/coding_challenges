import pytest
from main import no_overlap


def test_1():
    assert no_overlap([[1,2],[2,3],[3,4],[1,3]]) == 1, "Should be 1, because [1,3] can be removed and the rest of the intervals are non-overlapping."


def test_2():
    assert no_overlap([[[1,2],[1,2],[1,2]]) == 2, "Should be 2, because need to remove two [1,2] to make the rest of the intervals non-overlapping."

def test_3():
    assert no_overlap([[1,2],[2,3]]) == 0, "Should be 0, because don't need to remove any of the intervals since they're already non-overlapping."

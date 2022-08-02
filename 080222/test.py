"""
Tests
"""
import pytest
from main import permute


def test_one():
    assert permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], "Should be [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"

def test_two():
    assert permute([0,1]) == [[0,1],[1,0]], "Should be [[0,1],[1,0]]"
    
def test_three():
    assert permute([1]) == [[1]], "Should be [[1]]"


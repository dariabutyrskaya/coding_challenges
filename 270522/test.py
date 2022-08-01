import pytest 
from remove-nth-cell import product_except_self

def test_1():
    assert product_except_self([1,2,3,4]) == [24,12,8,6], "Should be 24,12,8,6"

def test_2():
    assert product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0], "Should be 0,0,9,0,0"


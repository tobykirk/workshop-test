from mysoftware import *

def test_square_integers():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-1) == 1
    assert square(3) == 9

def test_coulomb():
    assert coulomb(1.) == 1.0
    assert coulomb(-1.) == 1.0
    assert coulomb(5.0) == 0.2
    assert coulomb(13.0) == coulomb(-13.0)
    assert coulomb(0.0) == 'Inf'

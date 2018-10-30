import numpy as np


def square(x):
    return x**2

def coulomb(r):
    assert type(r) in [float, int], "You passed an invalid argument"
#    if r != 0.0:
    try:
        return 1/abs(r)
    except:
        return 'Inf'

def CentralDifference(f,x,h):
    #approx of f'(x)
    return (f(x+h)-f(x-h))/(2*h)


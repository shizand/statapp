# Copyright (c) 2023 Matthew Rocklin
# All rights reserved.
# This source code is distributed under the terms of the BSD license,
# which allows you to use, modify, and distribute it
# as long as you comply with the license terms.

# In addition, this code has been modified by Maxim Slipenko and
# is now also licensed under the GPL-3.0.
# See the GPL-3.0 license for details.

import itertools
from numpy import linalg, zeros, ones, hstack, asarray
from sympy import symbols, Mul, Add, S


def basisVector(n, i):
    """ Return an array like [0, 0, ..., 1, ..., 0, 0]

    >>> from statapp._vendor.multipolyfit import basisVector
    >>> basis_vector(3, 1)
    array([0, 1, 0])
    >>> basisVector(5, 4)
    array([0, 0, 0, 0, 1])
    """
    x = zeros(n, dtype=int)
    x[i] = 1
    return x


def asTall(x):
    """ Turns a row vector into a column vector """
    return x.reshape(x.shape + (1,))


def multipolyfit(xs, y, deg, full=False, modelOut=False, powersOut=False):
    # pylint: disable-msg=too-many-locals
    """
    Least squares multivariate polynomial fit

    Fit a polynomial like ``y = a**2 + 3a - 2ab + 4b**2 - 1``
    with many covariates a, b, c, ...

    Parameters
    ----------

    xs : array_like, shape (M, k)
         x-coordinates of the k covariates over the M sample points
    y :  array_like, shape(M,)
         y-coordinates of the sample points.
    deg : int
         Degree o fthe fitting polynomial
    modelOut : bool (defaults to True)
         If True return a callable function
         If False return an array of coefficients
    powersOut : bool (defaults to False)
         Returns the meaning of each of the coefficients in the form of an
         iterator that gives the powers over the inputs and 1
         For example if xs corresponds to the covariates a,b,c then the array
         [1, 2, 1, 0] corresponds to 1**1 * a**2 * b**1 * c**0

    See Also
    --------
        numpy.polyfit

    """
    # pylin
    y = asarray(y).squeeze()
    # rows = y.shape[0]
    xs = asarray(xs)
    numCovariates = xs.shape[1]
    xs = hstack((ones((xs.shape[0], 1), dtype=xs.dtype) , xs))

    generators = [basisVector(numCovariates + 1, i)
                  for i in range(numCovariates+1)]

    # All combinations of degrees
    powers = [sum(x) for x in itertools.combinations_with_replacement(generators, deg)]

    # Raise data to specified degree pattern, stack in order
    a = hstack(asarray([asTall((xs ** p).prod(1)) for p in powers]))

    result = linalg.lstsq(a, y, rcond=None)
    beta = result[0]

    if modelOut:
        return mkModel(beta, powers)

    if powersOut:
        return beta, powers

    if full:
        return result, powers, a

    return beta


def mkModel(beta, powers):
    """ Create a callable python function out of beta/powers from multipolyfit

    This function is callable from within multipolyfit using the model_out flag
    """
    # Create a function that takes in many x values
    # and returns an approximate y value
    def model(*args):
        numCovariates = len(powers[0]) - 1
        if len(args) != numCovariates:
            raise ValueError(f"Expected {numCovariates} inputs")
        xs = asarray((1,) + args)
        return sum(coeff * (xs**p).prod()
                             for p, coeff in zip(powers, beta))
    return model


def mkSympyFunction(beta, powers):
    terms = getTerms(powers)
    return Add(*[coeff * term for term, coeff in zip(terms, beta)])


def getTerms(powers):
    numCovariates = len(powers[0])
    xs = (S.One,) + symbols(f'x1:{numCovariates}')

    terms = [Mul(*[x ** deg for x, deg in zip(xs, power)]) for power in powers]
    return terms

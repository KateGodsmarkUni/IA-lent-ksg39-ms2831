"""Unit test for the analysis module"""

import numpy as np
import matplotlib

from floodsystem.analysis import *

def test_polyfit():
    # Find polynomial
    shift = 1
    order = 2
    input1 = [0, 1, 2, 3, 4]
    input2 = [2, 4, 6, 8, 10]
    num = matplotlib.dates.date2num(input1)
    coeff = np.polyfit(num - num[shift - 1], input2, order)
    poly1 = np.poly1d(coeff)

    # Get polynomial from function
    poly2, output_shift = polyfit(input1, input2, order)

    assert poly1 == poly2


def test_diff_polyfit():
    # Find polynomial
    shift = 1
    order = 2
    input1 = [0, 1, 2, 3, 4]
    input2 = [2, 4, 6, 8, 10]
    num = matplotlib.dates.date2num(input1)
    coeff = np.polyfit(num - num[shift - 1], input2, order)
    poly = np.poly1d(coeff)

    # Differentiate and evaluate polynomial
    diff_poly = np.polyder(poly, 1)
    diff_value1 = np.polyval(diff_poly, num[-1])

    # Get value from function
    diff_value2 = diff_polyfit(input1, input2, order)

    assert diff_value1 == diff_value2

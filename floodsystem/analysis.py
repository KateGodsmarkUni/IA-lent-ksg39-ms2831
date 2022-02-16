import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    
    '''This function creates a least-squares polynomial fit of degree to water level data given'''

    dates_num = matplotlib.dates.date2num(dates)
    coeff = np.polyfit(dates_num, levels, p)
    poly = np.poly1d(coeff)

    return(poly)
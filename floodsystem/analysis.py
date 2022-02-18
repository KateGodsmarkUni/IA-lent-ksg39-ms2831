import numpy as np
import matplotlib

#ALL FUNCTIONS HERE NEED TESTS FOR THEM

def polyfit(dates, levels, p):
    
    '''This function creates a least-squares polynomial fit of degree to water level data given'''

    datetime_shift = 1
    dates_num = matplotlib.dates.date2num(dates)
    coeff = np.polyfit(dates_num - dates_num[datetime_shift - 1], levels, p)
    poly = np.poly1d(coeff)

    return(poly, datetime_shift)

def diff_polyfit(dates, levels, p):

    '''This function finds the differential of the least-squares polynomial fit and returns the value'''
    '''of the differential for the latest water level reading time'''

    # Get polynomial
    poly, d0 = polyfit(dates, levels, p)
    dates_num = matplotlib.dates.date2num(dates)

    # Find differential and evaluate it for latest measurement
    diff_poly = np.polyder(poly, 1)

    diff_value = np.polyval(diff_poly, dates_num[-1])

    return diff_value

def assess_risk_level(higher_risk, lower_risk):

    '''This function uses input data split into stations with water level higher or lower'''
    '''than typical maximum to then assess the flood risk severity at that location'''

    # Set up lists for each level of risk
    low_risk = []
    moderate_risk = []
    high_risk = []
    severe_risk = []

    # Assess flood risk for stations with level above typical max
    for station in higher_risk:
        town = station[1]
        level_change = station[2]
        rel_water_level = station[3]
        if 1.0 < rel_water_level <= 1.2 and level_change < 0:
            low_risk.append(town)
        elif 1.0 < rel_water_level <= 1.2 and level_change > 0:
            moderate_risk.append(town)
        elif 1.2 < rel_water_level <= 1.6 and level_change < 0:
            moderate_risk.append(town)
        elif 1.2 < rel_water_level <= 1.6 and level_change > 0:
            high_risk.append(town)
        elif 1.6 < rel_water_level <= 2.0 and level_change < 0:
            high_risk.append(town)
        elif 1.6 < rel_water_level <= 2.0 and level_change > 0:
            severe_risk.append(town)
        elif rel_water_level > 2.0:
            severe_risk.append(town)
        elif level_change == "Invalid past data":
            pass
    
    # Assess flood risk for stations with level below typical max
    for station in lower_risk:
        town = station[1]
        low_risk.append(town)
    
    return(low_risk, moderate_risk, high_risk, severe_risk)
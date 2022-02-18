import datetime
from operator import mod
from re import M

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels, sort_station_risk_data
from floodsystem.analysis import assess_risk_level

def run():

    """Requirements for Task 2G"""

    # Build station list
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get data required for each station to assess flood risk, separating stations with valid and invalid data first
    d = 7 #number of past days to get river data for to assess flood severity
    p = 10 #polyfit order
    higher_risk, lower_risk, invalid_data = sort_station_risk_data(stations, d, 10)

    #Assess flood risk for every location and categorize towns based on risk level
    low_risk, moderate_risk, high_risk, severe_risk = assess_risk_level(higher_risk, lower_risk)

    #Need to put in code that will give risk data in reasonable format, rather than just listing all stations

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
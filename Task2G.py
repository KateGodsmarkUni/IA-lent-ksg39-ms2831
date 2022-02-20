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
    d = 4 #number of past days to get river data for to assess flood severity
    p = 4 #polyfit order
    higher_risk, lower_risk = sort_station_risk_data(stations, d, p)

    # Assess flood risk for every location and categorize towns based on risk level
    low_risk, moderate_risk, high_risk, severe_risk = assess_risk_level(higher_risk, lower_risk)

    # Give list of towns at severe risk of flooding
    print("----------------------------------------------------------------------")
    print("Towns which have been assessed to have severe risk of flooding(in descending order of severity):")
    for location in severe_risk:
        print(location)
    print("----------------------------------------------------------------------")
    
    # Find flood risk of towns that are not in severe risk of flooding
    request_town = input("Enter name of town to see its flood risk level, enter n to exit:")

    while request_town != "n":
        if request_town in low_risk:
            print("Low risk of flooding")
        elif request_town in moderate_risk:
            print("Moderate risk of flooding")
        elif request_town in high_risk:
            print("High risk of flooding")
        elif request_town in severe_risk:
            print("Severe risk of flooding")
        else:
            print("Data unavailable")
        request_town = input("Enter name of town to see its flood risk level, enter n to exit:")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
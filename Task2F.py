import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit

def run():

    """Requirements for Task 2F"""

    # Build station list
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get data of 5 stations with highest relative water levels 
    highest_stations = stations_highest_rel_level(stations, 5)

    # Get water level data for last d days
    d = 2
    #below function will only output 4 graphs, ignoring Letcombe Bassett - need to add code later that does it correctly!!!
    for station in highest_stations:
        print(station.name)
        if station.name != "Letcombe Bassett":
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=d))
            plot_water_level_with_fit(station, dates, levels, 4)

#Letcombe Bassett always has no data retrieved using fetch_measure_levels
#Find out if that is an error in program that should be corrected, or left alone
#Or if station should be omitted altogether and the 6th station to be used

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
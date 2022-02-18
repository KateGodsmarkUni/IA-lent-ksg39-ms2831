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

    # Get data of 5 stations with highest relative water levels, discarding stations with invalid data
    d = 2
    all_stations = stations_highest_rel_level(stations, 900)
    highest_stations = []
    i = 0
    for station in all_stations:
        date_check, level_check = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=d))
        if bool(date_check)==True:
            if i < 5:
                highest_stations.append(station)
                i += 1
            else:
                break
        else:
            print(station.name, "has been excluded due to invalid data for the past", d, "days")
    
    # Get water level data for last d days
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
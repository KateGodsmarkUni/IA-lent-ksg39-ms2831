import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

def run():

    """Requirements for Task 2E"""

    # Build station list
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get data of 5 stations with highest relative water levels 
    highest_stations = stations_highest_rel_level(stations, 5)
    for highest_station in highest_stations:
        print(highest_station.name)

    # Get water level data for last d days
    d = 10
    for station in highest_stations:
        print(station.name)
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=d))
        for date, level in zip(dates, levels):
            print(date, level)
        #plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()


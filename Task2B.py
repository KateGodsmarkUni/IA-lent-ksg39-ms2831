from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    high_stations = stations_level_over_threshold(stations, 0.8)
    for high_station in high_stations:
        name = high_station[0].name
        level = high_station[1]
        print(name, level)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
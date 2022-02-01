from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    
    """Requirements for Task 1F"""

    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    inconsistent_stations_order = sorted(inconsistent_stations)
    print(inconsistent_stations_order)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number, stations_by_river
from floodsystem.utils import sorted_by_key

def run():

    """Requirements for Task 1E"""

    stations = build_station_list()
    rivers_station_number = rivers_by_station_number(stations, 9)
    print(rivers_station_number)
    

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
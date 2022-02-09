from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.utils import sorted_by_key

def run():

    """Requirements for Task 1C"""

    # Build list of stations
    all_stations = build_station_list()

    #cambridge centre
    centre = (52.2053, 0.1218)


    stations = (stations_within_radius(all_stations, centre, 10))
    print(f'The stations within 10km are: {sorted_by_key(stations, 0)}')

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
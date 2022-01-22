from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.utils import sorted_by_key

def run():

    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print(len(rivers))
    sorted_rivers = sorted_by_key(rivers, 0)
    print(sorted_rivers[:10])

    rivers_and_stations = stations_by_river(stations)

    aire_stations = rivers_and_stations["River Aire"]
    aire_station_names = []
    for station in aire_stations:
        aire_station_names.append(station.name)
    print(f'Stations on the River Aire are: {sorted_by_key(aire_station_names, 0)}')

    cam_stations = rivers_and_stations["River Cam"]
    cam_station_names = []
    for station in cam_stations:
        cam_station_names.append(station.name)
    print(f'Stations on the River Cam are: {sorted_by_key(cam_station_names, 0)}')

    thames_stations = rivers_and_stations["River Thames"]
    thames_station_names = []
    for station in thames_stations:
        thames_station_names.append(station.name)
    print(f'Stations on the River Thames are: {sorted_by_key(thames_station_names, 0)}')



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
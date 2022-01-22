
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    # Build list of stations
    stations = build_station_list()

    #example place
    p = (52.2, 0.115)

    sorted_stations = (stations_by_distance(stations, p))
    print(f'The closest stations are: {sorted_stations[:10]}')
    print(f'The furthest stations are: {sorted_stations[-10:]}')

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
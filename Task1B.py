
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():

    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    #example places
    p = (52.2053, 0.1218)
    #p = (51.47, -0.609)

    station_distances = (stations_by_distance(stations, p))
    sorted_stations = []

    #creating a new list of tuples to add in the town by searching through the original list of stations

    for station_distance in station_distances:
        for station in stations:
            if station_distance[0] == station.name:
                sorted_stations.append((station.name, station.town, station_distance[1]))
                break

    print(f'The closest stations are: {sorted_stations[:10]}')
    print(f'The furthest stations are: {sorted_stations[-10:]}')

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():

    # Build list of stations
    stations = build_station_list()

    p = (51.47, -0.609)
    sorted_stations = stations_by_distance(stations, p)
    assert len(stations) == len(sorted_stations)
    for i in range(len(stations) - 1):
       assert sorted_stations[i][2] <= sorted_stations[i + 1][2]

    
#def test_stations_within_radius():


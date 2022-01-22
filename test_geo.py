"""Unit test for the geo module"""

from floodsystem.geo import *
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():

    # Build list of stations
    stations = build_station_list()

    p = (51.47, -0.609)
    sorted_stations = stations_by_distance(stations, p)
    assert len(stations) == len(sorted_stations)
    for i in range(len(stations) - 1):
       assert sorted_stations[i][1] <= sorted_stations[i + 1][1]

    
def test_stations_within_radius():
    
     # Build list of stations
    stations = build_station_list()

    p = (51.47, -0.609)
    stations_within = stations_within_radius(stations, p, 10)

    # comparing with a known list of stations within 10km of a certain point
    assert len(stations_within) == 27


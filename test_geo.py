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


def test_rivers_with_station():

    # Build list of stations
    stations = build_station_list()

    rivers  = rivers_with_station(stations)

    assert len(rivers) != 0


def test_stations_by_river():

     # Build list of stations
    stations = build_station_list()

    rivers_and_stations = stations_by_river(stations)
    assert len(rivers_and_stations) == len(rivers_with_station(stations))

    total = 0
    for value in rivers_and_stations.values():
        assert len(value)
        total += len(value)
    assert total == len(stations)

def test_rivers_by_station_number():

    #Build list of stations
    stations = build_station_list()
    N = 9
    
    #Get results of rivers with most stations
    rivers_station_number = rivers_by_station_number(stations, N)
    
    #Test function output
    n = 0
    i = 0
    for river in rivers_station_number:
        if i != 0:
            if river[1] < rivers_station_number[i-1][1]:
                i += 1
                n += 1
            elif river[1] == rivers_station_number[i-1][1]:
                i += 1
        elif i == 0:
            i += 1
            n += 1
    assert n == N


"""Unit test for the flood module"""
from floodsystem.flood import *
from floodsystem.stationdata import build_station_list, update_water_levels


def test_stations_level_over_threshold():
    
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    stations_above = stations_level_over_threshold(stations, 0.9)
    for i in range(len(stations_above) - 1):
        assert stations_above[i][1] >= stations_above[i + 1][1]
        assert stations_above[i][1] >= 0.9


def test_stations_highest_rel_level():

     # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    highest_n = stations_highest_rel_level(stations, 10)
    assert len(highest_n) == 10

    for i in range(len(highest_n) - 1):
        assert highest_n[i].relative_water_level() > highest_n[i + 1].relative_water_level()

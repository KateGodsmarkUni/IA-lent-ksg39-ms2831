# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the stationdata module"""

from floodsystem.stationdata import *


def test_build_station_list():
    """Test building list of stations"""
    station_list = build_station_list()
    assert len(station_list) > 0


def test_update_level():
    """Test update to latest water level"""

    # Build list of stations
    stations = build_station_list()
    for station in stations:
        assert station.latest_level is None

    # Update latest level data for all stations
    update_water_levels(stations)
    counter = 0
    for station in stations:
        if station.latest_level is not None:
            counter += 1

    assert counter > 0

def test_sort_station_risk_data():
    """Test first part of assessing risk of flooding at stations"""

    # Build list of stations
    stations = build_station_list()

    test_stations = [stations[0], stations[1]]

    higher_risk_result, lower_risk_result = sort_station_risk_data(test_stations, 2, 4)
    
    if bool(higher_risk_result) == True:
        assert higher_risk_result[-1][2] > 1.0
    
    if bool(lower_risk_result) == True:
        assert lower_risk_result[0][1] < 1.0

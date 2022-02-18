# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides interface for extracting statiob data from
JSON objects fetched from the Internet and

"""

import datetime

from . import datafetcher
from .station import MonitoringStation
from .analysis import diff_polyfit
from .utils import sorted_by_key
from .datafetcher import fetch_measure_levels


def build_station_list(use_cache=True):
    """Build and return a list of all river level monitoring stations
    based on data fetched from the Environment agency. Each station is
    represented as a MonitoringStation object.

    The available data for some station is incomplete or not
    available.

    """

    # Fetch station data
    data = datafetcher.fetch_station_data(use_cache)

    # Build list of MonitoringStation objects
    stations = []
    for e in data["items"]:
        # Extract town string (not always available)
        town = None
        if 'town' in e:
            town = e['town']

        # Extract river name (not always available)
        river = None
        if 'riverName' in e:
            river = e['riverName']

        # Attempt to extract typical range (low, high)
        try:
            typical_range = (float(e['stageScale']['typicalRangeLow']),
                             float(e['stageScale']['typicalRangeHigh']))
        except Exception:
            typical_range = None

        try:
            # Create mesure station object if all required data is
            # available, and add to list
            s = MonitoringStation(
                station_id=e['@id'],
                measure_id=e['measures'][-1]['@id'],
                label=e['label'],
                coord=(float(e['lat']), float(e['long'])),
                typical_range=typical_range,
                river=river,
                town=town)
            stations.append(s)
        except Exception:
            # Not all required data on the station was available, so
            # skip over
            pass

    return stations


def update_water_levels(stations):
    """Attach level data contained in measure_data to stations"""

    # Fetch level data
    measure_data = datafetcher.fetch_latest_water_level_data()

    # Build map from measure id to latest reading (value)
    measure_id_to_value = dict()
    for measure in measure_data['items']:
        if 'latestReading' in measure:
            latest_reading = measure['latestReading']
            measure_id = latest_reading['measure']
            measure_id_to_value[measure_id] = latest_reading['value']

    # Attach latest reading to station objects
    for station in stations:

        # Reset latestlevel
        station.latest_level = None

        # Atach new level data (if available)
        if station.measure_id in measure_id_to_value:
            if isinstance(measure_id_to_value[station.measure_id], float):
                station.latest_level = measure_id_to_value[station.measure_id]

def sort_station_risk_data(stations, d, p):

    '''This function uses station data to split stations into higher risk(water level above typical '''
    '''maximum), lower risk(water level below typical max) and invalid data stations'''
    
    # Set up lists 
    higher_flood_risk = []
    lower_flood_risk = []
    invalid_data = []

    # Calculate and sort data needed to assess flood risk level
    for station in stations:
        try:
            if station.relative_water_level() > 1.0:
                dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=d))
                if bool(dates)==True:
                    level_change = diff_polyfit(dates, levels, p)
                else:
                    level_change = "Invalid past data"
                higher_flood_risk.append([station.name, station.town, level_change, station.relative_water_level()])
            else:
                lower_flood_risk.append([station.name, station.town, station.relative_water_level()])
        except:
            invalid_data.append([station.name, station.town])
    
    # Sort lists into decreasing order of relative water level
    higher_risk_sorted = sorted_by_key(higher_flood_risk, 3)
    lower_risk_sorted = sorted_by_key(lower_flood_risk, 2)

    higher_risk_sorted.reverse()
    lower_risk_sorted.reverse()

    return(higher_risk_sorted, lower_risk_sorted, invalid_data)
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import *
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):

    '''A function that returns a list of (station, distance) tuples, where distance (float) is the distance of the station (MonitoringStation) 
    from the coordinate p, sorted by distance.'''

    station_distances = []
    for station in stations:
        distance = haversine(station.coord, p)
        station_distances.append((station.name, distance))
    station_distances = sorted_by_key(station_distances, 1)
    return  station_distances
    

def stations_within_radius(stations, centre, r):

    '''A function that returns a list of all stations within r of the centre co-ordinate'''

    stations_within_r = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            stations_within_r.append(station.name)
    return stations_within_r

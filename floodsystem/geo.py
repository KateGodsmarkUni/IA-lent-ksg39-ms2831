# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import *
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    station_distances = []
    for station in stations:
        distance = haversine(station.coord, p)
        station_distances.append((station.name, station.town, distance))
    station_distances = sorted_by_key(station_distances, 2)
    return  station_distances
    

def stations_within_radius(stations, centre, r):
    stations_within_r = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            stations_within_r.append(station.name)
    return stations_within_r

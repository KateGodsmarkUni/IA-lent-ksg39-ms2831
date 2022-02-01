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

def rivers_with_station(stations):

    '''A function to return a set with the names of the rivers with a monitoring station from the list'''

    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers 

def stations_by_river(stations):

    '''A function to return a dict with the names of the rivers and its monitoring stations'''

    rivers_and_stations = {}
    rivers = rivers_with_station(stations)
    for river in rivers:
        rivers_stations = []
        for station in stations:
            if river == station.river:
                rivers_stations.append(station)
        rivers_and_stations[river] =  rivers_stations
    return rivers_and_stations

def rivers_by_station_number(stations, N):

    '''A function that returns a list of the N rivers with the greatest number of monitoring stations'''
    
    #Get list of tuples containing rivers and number of monitoring stations
    rivers_station_number = []
    rivers = rivers_with_station(stations)
    for river in rivers:
        number_of_stations = 0
        for station in stations:
            if river == station.river:
                number_of_stations += 1
        rivers_station_number.append((river, number_of_stations))
    rivers_station_number_order = sorted_by_key(rivers_station_number, 1)

    #Get list of tuples containing rivers with the most stations - N is different number of stations at a river
    most_stations = []
    station_num_in_list = 1
    river_in_list = 1
    while station_num_in_list <= N:
        new_river = rivers_station_number_order[len(rivers_station_number_order)-river_in_list]
        if station_num_in_list == 1:
            most_stations.append(new_river)
            station_num_in_list += 1
            river_in_list += 1
        elif station_num_in_list > 1:
            if new_river[1] == most_stations[river_in_list-2][1]:
                most_stations.append(new_river)
                river_in_list += 1
            elif new_river[1] < most_stations[river_in_list-2][1]:
                most_stations.append(new_river)
                station_num_in_list += 1
                river_in_list += 1        
    return most_stations
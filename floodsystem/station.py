# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        try:
            typical_min = self.typical_range[0]
            typical_max = self.typical_range[1]
        except TypeError:
            return False
        if typical_min < typical_max:
            return True
        else:
            return False
        
    def relative_water_level(self):
        if self.typical_range_consistent() :
            try:
                typical_min = self.typical_range[0]
                typical_max = self.typical_range[1]
                latest = self.latest_level
                difference  = latest - typical_min
                ratio = difference / (typical_max - typical_min)
            except TypeError:
                return None
            return ratio


def inconsistent_typical_range_stations(stations):
    
    '''A function that returns a list of stations with inconsistent typical range data'''

    inconsistent_stations = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_stations.append(station.name)
    return inconsistent_stations


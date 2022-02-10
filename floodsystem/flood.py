from .utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol):
    '''Function that returns stations which have a relative water level over the threshold'''
    high_stations = []
    for station in stations:
        try:
            if station.relative_water_level() > tol:
                station_info = (station, station.relative_water_level())
                high_stations.append(station_info)
        except:
            pass
    return sorted_by_key(high_stations, 1, reverse=True)


def stations_highest_rel_level(stations, n):
    ''' Function that returns a list of the N stations (objects) with the highest relative water level.'''
    all_stations = stations_level_over_threshold(stations, 0)
    highest_n = []
    for i in range(n):
        highest_n.append(all_stations[i][0])
    return highest_n


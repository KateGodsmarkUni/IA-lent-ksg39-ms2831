from .utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol):
    high_stations = []
    for station in stations:
        try:
            if station.relative_water_level() > tol:
                station_info = (station, station.relative_water_level())
                high_stations.append(station_info)
        except:
            pass
    return sorted_by_key(high_stations, 1, reverse=True)
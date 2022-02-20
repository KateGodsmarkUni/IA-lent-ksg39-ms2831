"""Unit test for the plot module"""

import datetime
import matplotlib
import matplotlib.pyplot as plt
import os
from matplotlib.testing.decorators import image_comparison

from floodsystem.plot import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels


def test_plot_water_levels():
    # Build station list
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    station = stations[0]

    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
    plot_water_levels(station, dates, levels)
    plt.savefig("func_output.png")

    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()
    plt.savefig("test_output.png")
    
    image_comparison(["func_output.png", "test_output.png"])
    
    os.remove("func_output.png")
    os.remove("test_output.png")


def test_plot_water_level_with_fit():
    # Build station list
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    station = stations[0]

    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
    plot_water_level_with_fit(station, dates, levels, 5)
    plt.savefig("func_output.png")

    poly, d0 = polyfit(dates, levels, 5)
    dates_num = matplotlib.dates.date2num(dates)

    typical_min = station.typical_range[0]
    typical_max = station.typical_range[1]
    typical_min_list = np.full(len(dates), typical_min)
    typical_max_list = np.full(len(dates), typical_max)

    plt.plot(dates, levels, label = "Real data")
    plt.plot(dates, poly(dates_num - dates_num[d0 - 1]), label = "Least-squares polynomial fit")
    plt.plot(dates, typical_min_list, label = "Typical minimum level")
    plt.plot(dates, typical_max_list, label = "Typical maximum level")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.legend()
    plt.tight_layout()  
    plt.savefig("test_output.png")
    
    image_comparison(["func_output.png", "test_output.png"])
    
    os.remove("func_output.png")
    os.remove("test_output.png")

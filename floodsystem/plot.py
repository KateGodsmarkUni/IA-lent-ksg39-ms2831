import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from .analysis import polyfit

#ALL FUNCTIONS HERE NEED TESTS FOR THEM

def plot_water_levels(station, dates, levels):
    
    '''This function plots a graph of water levels over a period of time for a certain station'''
    
    # Plotting setup
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):

    '''This function plots a graph of water levels over a period of time for a certain station, along with its least-squares polynomial fit'''
    
    # Get polynomial for this data
    poly, d0 = polyfit(dates, levels, p)
    dates_num = matplotlib.dates.date2num(dates)

    # Get typical range of station and adapt format to plot it
    typical_min = station.typical_range[0]
    typical_max = station.typical_range[1]
    typical_min_list = np.full(len(dates), typical_min)
    typical_max_list = np.full(len(dates), typical_max)

    # Plot the real and polynomial data
    plt.plot(dates, levels, label = "Real data")
    plt.plot(dates, poly(dates_num - dates_num[d0 - 1]), label = "Least-squares polynomial fit")
    plt.plot(dates, typical_min_list, label = "Typical minimum level")
    plt.plot(dates, typical_max_list, label = "Typical maximum level")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.legend()
    plt.tight_layout()  
    plt.show()
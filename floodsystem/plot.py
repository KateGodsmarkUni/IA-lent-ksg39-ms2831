import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from .analysis import polyfit


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
    
    #Get polynomial for this data
    poly = polyfit(dates, levels, p)
    dates_num = matplotlib.dates.date2num(dates)

    #Plot the real and polynomial data
    plt.plot(dates, levels, label = "Real data")
    plt.plot(dates, poly(dates_num), label = "Least-squares polynomial fit")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.legend()
    plt.tight_layout()  
    plt.show()
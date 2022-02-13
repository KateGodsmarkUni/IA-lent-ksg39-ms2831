import matplotlib.pyplot as plt

from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    
    '''This function plots a graph of water levels for the past d days for a certain station'''
    
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
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json
import sys
import getopt
from earthquakes import Quake, QuakeData, calc_distance

file_path = ".\earthquakes.geojson"

if len(sys.argv) > 1:
    file_path = sys.argv[1]

path = Path(file_path)

try:
    geojason_dictionary = json.loads(path.read_text())
except FileNotFoundError:
    print("Error reading in JSON file")

quake_data = QuakeData(geojason_dictionary)
print("Earthquake Analyser")

######### Functions #########

def set_location_filter():
    """ Ask the user for a latitude, longitude, and distance and set a location filter on QuakeData accordingly."""
    pass

def set_property_filter():
    """ Ask the user for minimum values for significance, felt, and magnitude and set the property filter on QuakeData accordingly.
    Warn the user if no value is supplied for any of the properties. """
    pass

def clear_filters():
    """ Clear the filters on the QuakeData object and display the text 'cleared'."""
    pass

def display_quakes():
    """ Display all of the Quakes that satisfy the filters set as user-friendly strings."""
    pass

def display_exceptional_quakes():
    """ Display all of the Quakes that satisfy the filters set whose magnitude is greater
    than one standard deviation above the median quake magnitude as user-friendly strings."""
    pass

def display_magnitude_stats():
    """ Display the mean, median, and standard deviation of the magnitude of the filtered quakes. 
    Display the mode of the magnitude when magnitude is rounded down to whole numbers. """
    pass

def plot_quake_map():
    """ Display a scatter map of the filtered quakes where the size of the dots is equal to the magnitude of the quakes scaled. """
    pass

def plot_magnitude_chart():
    """ Display a bar chart of how many quakes of each whole number magnitude occurred amongst the filtered quakes. """
    pass

def quit():
    """ Quit the program. """
    print("Thanks! See you again soon.")
    sys.exit()

######### Prompting Users #########

prompt = "\nPlease pick one of the following options:"
prompt += "\n1) Set Location Filter"
prompt += "\n2) Set Property Filter"
prompt += "\n3) Clear Filters"
prompt += "\n4) Display Quakes"
prompt += "\n5) Display Exceptional Quakes"
prompt += "\n6) Display Magnitude Stats"
prompt += "\n7) Plot Quake Map"
prompt += "\n8) Plot Magnitude Chart"
prompt += "\n9) Quit"

while True:
    print(prompt)
    option = input("Enter your choice: ")

    try:
        option = int(option)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if option == 1:
        set_location_filter()
    elif option == 2:
        set_property_filter()
    elif option == 3:
        clear_filters()
    elif option == 4:
        display_quakes()
    elif option == 5:
        display_exceptional_quakes()
    elif option == 6:
        display_magnitude_stats()
    elif option == 7:
        plot_quake_map()
    elif option == 8:
        plot_magnitude_chart()
    elif option == 9:
        quit()
    else:
        print("Invalid option, please try again.")


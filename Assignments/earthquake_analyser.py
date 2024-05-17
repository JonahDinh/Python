import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json
import sys
from earthquakes import Quake, QuakeData, calc_distance

file_path = ".\earthquakes.geojson"

# https://www.askpython.com/python/python-command-line-arguments
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
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    distance = float(input("Enter distance: "))
    quake_data.set_location_filter(latitude, longitude, distance)

def set_property_filter():
    """ Ask the user for minimum values for significance, felt, and magnitude and set the property filter on QuakeData accordingly.
    Warn the user if no value is supplied for any of the properties. """
    
    min = input("Enter minimum magnitude:")

    if min:
        try:
            mag = float(min)
        except ValueError:
            print("Warning: Magnitude should be a numeric value.")
            return
    else:
        mag = None
        print("Warning: No magnitude filter has been set.")
    
    min = input("Enter minimum felt:")

    if min:
        try:
            felt = int(min)
        except ValueError:
            print("Warning: Felt should be an integer value.")
            return
    else:
        felt = None
        print("Warning: No felt filter has been set.")

    min = input("Enter minimum significance:")
    if min:
        try:
            sig = int(min)
        except ValueError:
            print("Warning: Significance should be an integer value.")
            return
    else:
        sig = None

    # Set the property filter
    if mag is None and felt is None and sig is None:
        print("Warning: No filter has been set.")
    else:
        quake_data.set_property_filter(mag, felt, sig)

def clear_filters():
    """ Clear the filters on the QuakeData object and display the text 'cleared'."""
    quake_data.clear_filter()
    print("Cleared the filters!")
    pass

def display_quakes():
    """ Display all of the Quakes that satisfy the filters set as user-friendly strings."""
    filtered_data_set = quake_data.get_filtered_array()
    for quake in filtered_data_set:
        print (quake[0])

def display_exceptional_quakes():
    """ Display all of the Quakes that satisfy the filters set whose magnitude is greater
    than one standard deviation above the median quake magnitude as user-friendly strings."""
    filtered_data_set = quake_data.get_filtered_array()
    for quake in filtered_data_set:
        print (quake[0])


def display_magnitude_stats():
    """ Display the mean, median, and standard deviation of the magnitude of the filtered quakes. 
    Display the mode of the magnitude when magnitude is rounded down to whole numbers. """
    filtered_data_set = quake_data.get_filtered_array()

    print(f"\nMean Magnitude: {np.mean(filtered_data_set['mag'])}")
    print(f"Median Magnitude: {np.median(filtered_data_set['mag'])}")
    print(f"Standard Deviation of Magnitude: {np.std(filtered_data_set['mag'])}")

    # https://www.statology.org/numpy-mode/ Used this to help understand how to find the mode.
    filtered_data_set['mag'] = np.floor(filtered_data_set['mag'])
    vals, counts = np.unique(filtered_data_set['mag'], return_counts=True)
    mode = np.argwhere(counts == np.max(counts))

    print(f"Mode Magnitude: {vals[mode].flatten().tolist()}")

def plot_quake_map():
    """ Display a scatter map of the filtered quakes where the size of the dots is equal to the magnitude of the quakes scaled. """
    pass

def plot_magnitude_chart():
    """ Display a bar chart of how many quakes of each whole number magnitude occurred amongst the filtered quakes. """
    pass

def quit():
    """ Quit the program. """
    print("\nThanks! See you again soon.")
    exit()

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


import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json

path = Path("./my_setting.json")

def calc_distance(lat1, long1, lat2, long2):
    """Returns the distance, in kilometers, between two lat/long coordinates"""
    #Using haversine formula, converting the JS to Python
    # const R = 6371e3; // metres
    R = 6371e3
    # const φ1 = lat1 * Math.PI/180; // φ, λ in radians
    phi1 = lat1 * np.pi/180
    # const φ2 = lat2 * Math.PI/180;
    phi2 = lat2 * np.pi/180
    # const Δφ = (lat2-lat1) * Math.PI/180;
    delta_phi = (lat2 - lat1) * np.pi / 180
    # const Δλ = (lon2-lon1) * Math.PI/180;
    delta_lambda = (long2 - long1) * np.pi / 180
    # const a = Math.sin(Δφ/2) * Math.sin(Δφ/2) + Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ/2) * Math.sin(Δλ/2);
    a = np.sin(delta_phi / 2) * np.sin(delta_phi / 2) + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) * np.sin(delta_lambda / 2)
    # const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    # const d = R * c; // in metres
    d = R * c

    return d / 1000

class QuakeData:
    """Information Data Set on Earthquake Data"""
    def __init__(self, geojson):
        """Constructor will go through the dictionary retrieve a list of earthquakes from the'features' entry in the dictionary"""
        self.quake_array = self._get_data_set(geojson)
        self._location_filter = None 
        self._property_filter = None

    def set_location_filter(self, latitude, longitude, distance):
        """"""
        self._location_filter = (latitude, longitude, distance)

    def set_property_filter(self, magnitude = None, felt = None, significance = None):
        """"""
        if magnitude is None and felt is None and significance is None:
            raise ValueError("At least one parameter must be supplied.")
        self._property_filter = (magnitude, felt, significance)

    def clear_filter(self):
        """"""
        self._location_filter = None
        self._property_filter = None


    def get_filtered_array(self):
        """Return a numpy array of filtered earthquakes."""
        filtered_quakes = self.quake_array.copy()
        filtered_quakes = self._apply_filters(filtered_quakes)
        return filtered_quakes
    
    def get_filtered_list(self):
        """Return a list of Quake objects containing only the earthquakes that pass the filters."""
        filtered_quakes = self.quake_array.copy()
        filtered_quakes = self._apply_filters(filtered_quakes)
        
        # Convert the filtered numpy array to a list of Quake objects
        filtered_quake_list = []
        for quake_data in filtered_quakes:
            quake_instance = Quake(quake_data['mag'], quake_data['time'], quake_data['felt'], quake_data['sig'], quake_data['q_type'], quake_data['coords'])
            filtered_quake_list.append(quake_instance)
        
        return filtered_quake_list

    def _get_data_set(self, geojson):
        """Helper function to parse the geojson dictionary into a Numpy array"""
        data_types = [
        ('quake', object),
        ('mag', float),
        ('felt', np.int32),
        ('sig', np.int32),
        ('lat', float),
        ('long', float)
        ]
    
        quakeDataList = []
        features = geojson.get('features') #Returns a list
        for feature in features:
            if feature.get('type') == "Feature":
                properties = feature.get('properties') #Dictionary
                geometry = feature.get('geometry') #Dictonary
                # The all key checks for true of each property - This means that it will make sure they have the "key" as well as a value that isn't null
                if all(key in properties and properties[key] != None for key in ['mag', 'time', 'felt', 'sig', 'type', 'magType']) and geometry.get('type') == 'Point'  and len(geometry.get('coordinates')) == 3:
                    mag = properties['mag']
                    time = properties['time']
                    felt = properties['felt']
                    sig = properties['sig']
                    q_type = properties['type']
                    coords = geometry['coordinates']
                    quake_instance = Quake(mag, time, felt, sig, q_type, coords)
                    quakeDataList.append((quake_instance, mag, felt, sig, coords[0], coords[1]))
        return np.array(quakeDataList, dtype=data_types)
    
    def _apply_filters(self, quake_data):
        """Apply location and property filters to the given data."""
        if self._location_filter:
            latitude, longitude, distance = self._location_filter
            # Calling the external calc_distance method - using this as a vectorized call
            quake_data = quake_data[calc_distance(quake_data['lat'], quake_data['long'], latitude, longitude) <= distance]

        if self._property_filter:
            magnitude, felt, significance = self._property_filter
            if magnitude is not None:
                quake_data = quake_data[quake_data['mag'] >= magnitude]
            if felt is not None:
                quake_data = quake_data[quake_data['felt'] >= felt]
            if significance is not None:
                quake_data = quake_data[quake_data['sig'] >= significance]

        return quake_data



class Quake:
    """Instance of an Earthquake"""
    def __init__(self, magnitude, time, felt, significance, q_type, coords):
        """Quake Constructor"""
        self.mag = magnitude
        self.time = time
        self.felt = felt
        self.sig = significance
        self.q_type = q_type
        self.lat = coords[0]
        self.long = coords[1]

    def __str__(self):
        """Override toString function"""
        return f"{self.mag} Magnitude Earthquake, {self.sig} Significance, felt by {self.felt} people in ({self.lat}, {self.long})"

    def get_distance_from(self, latitude, longitude):
        """Takes in a latitude and longitude and returns the number of km the Quake is from that point"""
        return calc_distance(latitude, longitude, self.lat, self.long)




    

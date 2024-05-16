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

 

    """Information on Earthquake Data"""
    def __init__(self, geojson):
        """Constructor will go through the dictionary retrieve a list of earthquakes from the'features' entry in the dictionary"""

        data_types = [
        ('quake', object),
        ('magnitude', float),
        ('felt', np.int32),
        ('significance', np.int32),
        ('lat', float),
        ('long', float)
        ]

        quakeDataList = []
        features = geojson.get('features') #Returns a list
        for feature in features:
            if feature.get('type') == "Feature":
                properties = feature.get('properties') #Dictionary
                geometry = feature.get('geometry') #Dictonary
                if all(key in properties and properties[key] is not None for key in ['mag', 'time', 'felt', 'sig', 'type', 'magType']) and geometry.get('type') == 'Point'  and len(geometry.get('coordinates')) == 3:
                    mag = properties['mag']
                    time = properties['time']
                    felt = properties['felt']
                    sig = properties['sig']
                    q_type = properties['type']
                    coords = geometry['coordinates']
                    quake_instance = Quake(mag, time, felt, sig, q_type, coords)
                    quakeDataList.append((quake_instance, mag, felt, sig, coords[0], coords[1]))
        self.quake_array = np.array(quakeDataList, dtype=data_types)
        self._location_filter = None #Tuple
        self._property_filter = None

    def set_location_filter(self, latitude, longitude, distance):
        """"""
        self._location_filter = (latitude, longitude, distance)


    def set_property_filter(self, magnitude, felt, significance):
        """"""
        if magnitude is None and felt is None and significance is None:
            raise ValueError("At least one parameter must be supplied.")
        self.property_filter = (magnitude, felt, significance)

    def clear_filter(self):
        """"""
        self._location_filter = None
        self._property_filter = None


    def get_filtered_array(self):
        """"""
        filtered_quakes = self.quake_array.copy()
        if self._location_filter:
            latitude, longitude, distance = self._location_filter
            filtered_quakes = filtered_quakes[calc_distance(filtered_quakes['lat'], filtered_quakes['long'], latitude, longitude) <= distance]
        if self._property_filter:
            magnitude, felt, significance = self._property_filter
            if magnitude != None:
                filtered_quakes = filtered_quakes[filtered_quakes['magnitude'] >= magnitude]
            if felt != None:
                filtered_quakes = filtered_quakes[filtered_quakes['felt'] >= felt]
            if significance != None:
                filtered_quakes = filtered_quakes[filtered_quakes['significance'] >= significance]
        return filtered_quakes
    
    def get_filtered_list(self):
        """Return a list of quake objects containing only the earthquakes that pass the filters set above"""
        pass


class Quake:
    """"""
    def __init__(self, magnitude, time, felt, significance, q_type, coords):
        """Quake Constructor"""
        self.magnitude = magnitude
        self.time = time
        self.felt = felt
        self.significance = significance
        self.q_type = q_type
        self.coords = coords

    def __str__(self):
        """Override toString function"""
        return f"{self.magnitude} Magnitude Earthquake, {self.significance} Significance, felt by {self.felt} people in ({self.coords[0]}, {self.coords[1]})"

    def get_distance_from(self, latitude, longitude):
        """Takes in a latitude and longitude and returns the number of km the Quake is from that point"""
        return calc_distance(latitude, longitude, self.coords[0], self.coords[1])



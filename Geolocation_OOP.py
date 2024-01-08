# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 02:43:35 2023

@author: Sebastian
"""
#pip install geopy
#pip install cartopy
#pip install folium
#conda install -c conda-forge basemap
#latittude and longitude: 46.7981762, 4.4255245

import folium
from geopy.geocoders import Nominatim
from IPython.display import HTML, display
import webbrowser
import os

class LocationMap:
    def __init__(self, user_agent="my_app_name"):
        self.geolocator = Nominatim(user_agent=user_agent)
        self.locations = []

    def get_user_location(self, coordinates):
        try:
            location = self.geolocator.reverse(coordinates)
            print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
            print(f"Address: {location.address}")
            return location
        except (AttributeError, TypeError) as e:
            print(f"Error: {e}")
            print("Unable to retrieve geolocation information. Please check your input or try again later.")
            return None

    def add_location(self, name, latitude, longitude, marker_color='blue'):
        self.locations.append({"name": name, "latitude": latitude, "longitude": longitude, "color": marker_color})

    def create_map(self, user_location, zoom_start=15):
        my_map = folium.Map(location=[user_location.latitude, user_location.longitude], zoom_start=zoom_start)
        return my_map

    def add_markers(self, my_map, user_location):
        # Add marker for user location (in red)
        popup_content_user = f"<strong>Your Location:</strong><br>{user_location.address}"
        folium.Marker(
            [user_location.latitude, user_location.longitude],
            popup=popup_content_user,
            icon=folium.Icon(color='red')
        ).add_to(my_map)

        # Add markers for other locations
        for loc in self.locations:
            popup_content_loc = f"<strong>{loc['name']}:</strong><br>({loc['latitude']}, {loc['longitude']})"
            folium.Marker(
                [loc['latitude'], loc['longitude']],
                popup=popup_content_loc,
                icon=folium.Icon(color=loc['color'])
            ).add_to(my_map)

    def save_and_display_map(self, my_map, file_name="my_location_map.html"):
        my_map.save(file_name)
        with open(file_name, "r") as f:
            html_content = f.read()
            display(HTML(html_content))


def Pharmacy():
    location_map = LocationMap()

    # User location
    user_location = location_map.get_user_location("46.7981762, 4.4255245")

    # Additional locations
    location_map.add_location("Hospital Du Creusot", 46.803000, 4.447830)
    location_map.add_location("Hospital Creusot Site Harfleur", 46.797710, 4.452310)
    location_map.add_location("Pharmacie des Acacias", 46.796310, 4.429500, 'green')
    location_map.add_location("Pharmacie des 4 Chemins", 46.795180, 4.425020, 'green')
    location_map.add_location("Pharmacie de la Molette", 46.8014317, 4.4194993, 'green')
    location_map.add_location("Pharmacie du Parc", 46.8062055, 4.4216474, 'green')

    # Create and customize the map
    my_map = location_map.create_map(user_location)
    location_map.add_markers(my_map, user_location)

    # Save and display the map
    location_map.save_and_display_map(my_map)
    map_file_path = "my_location_map.html"
    webbrowser.open(map_file_path)
    #os.remove(map_file_path)
    

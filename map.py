# GeoLocating Based on Data Added

import numpy as np
import pandas as pd

df = pd.read_csv('emergency-responce')

import requests
import json
import urllib

# https://developers.google.com/maps/documentation/geocoding/intro
base_url= "https://maps.googleapis.com/maps/api/geocode/json?"
AUTH_KEY = "AIzaSyD28syNmLrYKAM8LvQD7zyxTwsq4YIpP4Q"
# set up your search parameters - address and API key
parameters = {"address": "New York, New York", "key": AUTH_KEY}
# urllib.parse.urlencode turns parameters into url
print(f"{base_url}{urllib.parse.urlencode(parameters)}")

r = requests.get(f"{base_url}{urllib.parse.urlencode(parameters)}")
data = json.loads(r.content)
data

data.get("results")[0].get("geometry").get("location")
df = df[df['Longitude'].notna()]
df = df[df['Latitude'].notna()]

# import the library and its Marker clusterization service
import folium
from folium.plugins import MarkerCluster
# Create a map object and center it to the avarage coordinates to globe
globe = folium.Map(location=df[["Latitude", "Longitude"]].mean().to_list(), zoom_start=10)
# if the points are too close to each other, cluster them, create a cluster overlay with MarkerCluster, add to m
marker_cluster = MarkerCluster().add_to(globe)
# draw the markers and assign popup and hover texts
# add the markers the the cluster layers so that they are automatically clustered
for i,r in df.iterrows():
    location = (r["Latitude"], r["Longitude"])
    folium.Marker(location=location)\
    .add_to(marker_cluster)
# display the map
globe

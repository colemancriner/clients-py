import streamlit as st
import folium
from streamlit_folium import st_folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd
import numpy as np
import math


# Setup
st.set_page_config(page_title='My App',page_icon=':red_triangle_pointed_down:',layout='wide')

df = pd.read_csv('C:\\Users\\colem\\OneDrive\\Desktop\\clients-py\\Client Data - df.csv')

# Create a folium map object
zoom_lat = df['Latitude'].mean()
zoom_lon = df['Longitude'].mean()
m = folium.Map(location=[zoom_lat, zoom_lon], tiles='cartodbpositron', zoom_start=5)

# Plot zip codes on the map
markers = st.checkbox('Markers')
heat_map = st.checkbox('Heat Map')
marker_clusters = st.checkbox('Marker Clusters')
if markers:
    for i, row in df.iterrows():
        popup_value = str(row['Home Street'])
        tooltip_value = str(row['First Name']) + ' ' + str(row['Last Name'])
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=popup_value,
            tooltip=tooltip_value
        ).add_to(m)
elif heat_map:
    HeatMap(data=df[['Latitude', 'Longitude']], radius=17).add_to(m)
elif marker_clusters:
    mc = MarkerCluster()
    for idx, row in df.iterrows():
        if not math.isnan(row['Longitude']) and not math.isnan(row['Latitude']):
            mc.add_child(Marker([row['Latitude'], row['Longitude']]))
    m.add_child(mc)


# Render the folium map using streamlit
st_folium(m, width=1080, height=500)



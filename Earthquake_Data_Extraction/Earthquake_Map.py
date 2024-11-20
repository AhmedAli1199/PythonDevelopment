# import pandas as pd
# import folium
# from folium.plugins import MarkerCluster

# # For Streamlit integration (optional)
# import streamlit as st
# import streamlit_folium

# data = pd.read_csv('Earthquake_data.csv')

# m = folium.Map(location=[0, 0], zoom_start=2)

# def create_marker(row):
#   lat = row['latitude']
#   long = row['longitude']
#   magnitude = row['magnitude']
#   location = row['location']

#   popup_text = f"Magnitude: {magnitude}<br>Location: {location}"
#   radius = magnitude * 2
#   return folium.CircleMarker(
#     location=[lat, long],
#     radius=radius,
#     popup=popup_text,
#     color='red',
#     fill=True,
#     fill_color='red',
#     fill_opacity=0.7,
#     tooltip=location
#   )

  

# marker_cluster = MarkerCluster()

# for index, row in data.iterrows():
#   marker = create_marker(row)
#   marker_cluster.add_child(marker)

# m.add_child(marker_cluster)

# m.save('Earthquake_Map.html')





   

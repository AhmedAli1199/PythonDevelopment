
import requests


response = requests.get(
    'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
)

data = response.json()

master_list = []

for features in data['features']:
  magnitude = features['properties']['mag']
  location = features['properties']['place'].split(',')[0]
  longitude = features['geometry']['coordinates'][0]
  latitude = features['geometry']['coordinates'][1]
  dict = {
      'magnitude': magnitude,
      'location': location,
      'longitude': longitude,
      'latitude': latitude
  }
  master_list.append(dict)

with open('Earthquake_data.csv','w') as file:
  file.write('magnitude,location,longitude,latitude\n')
  for dict in master_list:
    file.write(f"{dict['magnitude']},{dict['location']},{dict['longitude']},{dict['latitude']}\n")
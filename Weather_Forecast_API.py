#Written by: Ahmed Ali
#Retrieve Weather Forecast Data for next 5 days from OpenWeather Api #based on city and 
#store in a file

import requests


def get_weather_data(city, API_key='c98eb50389c22cd88756d85efb8b4df1'):

  url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}'
  r = requests.get(url)
  content = r.json()
 
  data = ""
  count = content["cnt"]
  x = 0
  while x < count:
    temperature = content["list"][x]["main"]["temp"]
    time = content["list"][x]["dt_txt"]
    condition = content["list"][x]["weather"][0]["description"]
    data = data + f"{city}, {time}, {temperature}, {condition}\n"
    x = x + 1

  return data


def make_file():
  with open('weather_data.txt', 'a') as file:
    file.write('City, Time, Temperature, Condition\n')
    content = get_weather_data('London')
    file.write(content)


print(make_file())

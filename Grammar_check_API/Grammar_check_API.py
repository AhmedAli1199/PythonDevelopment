import requests

url = 'https://api.languagetool.org/v2/check'
data = {
  'text': 'Tis is a nixe day!',
  'language': 'en-US'
}

response = requests.post(url, data=data)
result = response.json()
errors = result['matches']
for error in errors:
  print(error['message'])
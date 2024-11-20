from flask import Flask, jsonify

from bs4 import BeautifulSoup
import requests

def get_currency_rate(from_currency, to_currency):
  url = f'https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])

  return rate

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency_rate(in_cur, out_cur)
    result = {'input_currency': in_cur, 'output_currency': out_cur, 'rate': rate}
    return jsonify(result)


app.run(host='0.0.0.0')
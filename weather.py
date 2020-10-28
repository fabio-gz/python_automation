"""
Prints the weather for the location specified
"""
import json
import requests
import sys
import config

APPID = config.api_key

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (
    location, APPID)

response = requests.get(url)
response.raise_for_status()

# print(response.text)
weatherdata = json.loads(response.text)

w = weatherdata['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

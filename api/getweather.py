# -*- coding: utf-8 -*-

import requests
import json
from flask import jsonify
header = {'Content-type': 'application/json'}
host = "46.101.200.118"


## enter long + lat
## returns weather data
## may return 405
def getWeather(lat, long):
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=6ea09d3d72b1feea0882f57858714717'.format(
        str(lat), str(long))
    request = requests.post(url, headers=header).text
    responsedict = json.loads(request)
    try:
        weather = responsedict['weather'][0]['main']
        weatherdesc = responsedict['weather'][0]['description']
        windspeed = responsedict['wind']['speed']
        temperature = str(int(responsedict['main']['temp']) - 273.15)

        rain = 0.0
        if 'rain' in responsedict:
            rain = float(responsedict['rain']['3h'])

        snow = 0.0
        if 'snow' in responsedict:
            snow = float(responsedict['snow']['3h'])

        response = {
            'weather': weather,
            'weatherdesc': weatherdesc,
            'windspeed': windspeed,
            'temperature': temperature,
            'rain': rain,
            'snow': snow
        }
    except Exception:
        response = responsedict
    return response


print getWeather(63.430515, 10.3950530)
#print getWeather(12, 12)

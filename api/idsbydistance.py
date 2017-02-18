# -*- coding: utf-8 -*-

import requests
import json
from flask import jsonify
header = {'Content-type': 'application/json'}
host = "46.101.200.118"


## enter long + lat + maxdistance
## returns ids in list by distance
## may return 405
def getIdsByDistance(lat, long, maxdistance):
    url = 'http://api.visitnorway.com/products?latitude={}&longitude={}&maxdistance={}&limit=10000'.format(
        lat, long, maxdistance)
    request = requests.get(url, headers=header).text
    responsedict = json.loads(request)
    response = []
    for x in responsedict:
        try:
            if x['id'] != None:
                response.append(x['id'])
        except:
            print "Could not find id"
    return response

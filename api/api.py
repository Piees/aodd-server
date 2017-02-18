# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_restful import Resource, Api
from getweather import getWeather
from flask_cors import CORS, cross_origin
from models import Categories, Product, db
from idsbydistance import getIdsByDistance
import json

app = Flask(__name__)
CORS(app)
api = Api(app)


class getsWeather(Resource):
    def get(self, lat, long):
        response = getWeather(lat, long)
        return response


## for pins return all
class getProducts(Resource):
    def get(self):
        request = Product.query.all()
        response = []
        for x in request:
            x.__dict__.pop("_sa_instance_state")
            response.append(x.__dict__)
        return response


class getProductsByDistance(Resource):
    def get(self, lat, long, distance):
        idslist = getIdsByDistance(lat, long, distance)
        response = []
        for x in idslist:
            print x
            temp = Product.query.filter_by(id=x).first()
            if temp != None:
                k = temp.__dict__
                k.pop("_sa_instance_state")
                response.append(k)
            print temp
        return response


'''
class getProductsByDistanceAndCategory(Resource):
    def get(self, lat, long, distance, category):
        idslist = getIdsByDistance(lat, long, distance)
        response = []
        for x in idslist:
            print x
            catName = Categories.query.filter_by(name=category).all()
            catlist = []
            temp = Product.query.filter_by(id=x).first()
            if temp != None:
                k = temp.__dict__
                k.pop("_sa_instance_state")
                response.append(k)
            print temp
        return response'''

api.add_resource(getProducts, '/api/products')
api.add_resource(getProductsByDistance,
                 '/api/products/<string:lat>/<string:long>/<string:distance>')
api.add_resource(getsWeather, '/api/getweather/<string:lat>/<string:long>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

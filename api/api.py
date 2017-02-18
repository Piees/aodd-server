# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_restful import Resource, Api
from getweather import getWeather
from flask_cors import CORS, cross_origin
from models import Categories, Product, db, User, TrackEvent
from idsbydistance import getIdsByDistance
import json

app = Flask(__name__)
CORS(app)
api = Api(app)


class postTrackEvent(Resource):
    def post(self, lat, long, deviceid, productid):
        trackE = TrackEvent(lat, long, deviceid, productid)
        db.session.add(trackE)
        db.session.commit()
        response = trackE.id
        return {'TrackEven created with id: ': response}


class getCategories(Resource):
    def get(self):
        request = Categories.query.all()
        response = []
        for x in request:
            x.__dict__.pop("_sa_instance_state")
            response.append(x.__dict__)
        return response


class getCategory(Resource):
    def get(self, id):
        request = Categories.query.filter_by(id=id).first()
        request.__dict__.pop("_sa_instance_state")
        response = request.__dict__
        return response


class userByDeviceid(Resource):
    def get(self, deviceid):
        request = User.query.filter_by(deviceid=deviceid).first()
        request.__dict__.pop("_sa_instance_state")
        response = request.__dict__
        return response

    def post(self, deviceid):
        usr = User(deviceid)
        db.session.add(usr)
        db.session.commit()
        response = usr.deviceid
        return {'User created with id: ': response}


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


api.add_resource(getCategory, '/api/categories/<string:id>')
api.add_resource(
    postTrackEvent,
    '/api/trackevent/<string:lat>/<string:long>/<string:deviceid>/<string:productid>'
)
api.add_resource(getCategories, '/api/categories')
api.add_resource(userByDeviceid, '/api/users/<string:deviceid>')
api.add_resource(getProducts, '/api/products')
api.add_resource(getProductsByDistance,
                 '/api/products/<string:lat>/<string:long>/<string:distance>')
api.add_resource(getsWeather, '/api/getweather/<string:lat>/<string:long>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

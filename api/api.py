from flask import Flask
from flask_restful import Resource, Api
from getweather import getWeather

app = Flask(__name__)
api = Api(app)


class getsWeather(Resource):
    def get(self, lat, long):
        response = getWeather(lat, long)
        return response


api.add_resource(getsWeather, '/api/getweather/<string:lat>/<string:long>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

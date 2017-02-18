# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import MySQLdb
import config
from getweather import getWeather

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "mysql://" + config.user + ":" + config.password + "@" + config.database + "/" + config.schema
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    deviceid = db.Column(db.Text(255), primary_key=True)
    name = db.Column(db.Text(255))
    email = db.Column(db.Text(255))
    age = db.Column(db.INTEGER)
    gender = db.Column(db.Text(255))
    points = db.Column(db.INTEGER)
    occupation = db.Column(db.Text(255))
    city = db.Column(db.Text(255))

    def __repr__(self):
        return "<User(deviceid={})>".format(self.deviceid)

    def __init__(self, deviceid):
        self.deviceid = deviceid


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.Text(255))
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    image = db.Column(db.Text(255))
    alternativeText = db.Column(db.Text(255))
    avgpoints = db.Column(db.INTEGER, default=0)

    categoriesid = db.Column(db.INTEGER, db.ForeignKey('categories.id'))
    categories = db.relationship(
        'Categories', backref=db.backref(
            'product', lazy='dynamic'))


class Categories(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.Text(255))
    code = db.Column(db.Text(255))

#[{"id":"7651",
#"name":"Ådneram Cabin",
#"geoLocation":{"latitude":59.01785,"longitude":6.93066,"elevation":0},
#"image":{"url":"http://media.tellus.no/images/?d=354&p=758&t=1",
#"alternativeText":"Ådneram Turisthytte","copyright":"Ådneram Turisthytte"},"hasFoodPrints":false,"hasGreenTravel":false,

#"categories":[{
#"id":"23",
#"name":"Hotels & More","code":null}],
#"owner":"Lister Reiseliv","ownerId":null,"address":"Undergangen v/Rogaland Teater","contact":{"address":"Undergangen v/Rogaland Teater","email":"informasjon@stavanger-turistforening.no","fax":null,"mobile":null,"phone":" +47 51840200","streetAddress":null,"postalCode":"4001","city":"Sirdal","web":"http://www.stavanger-turistforening.no","bookingUrl":"","county":{"code":11,"name":"ROGALAND"},"municipality":{"code":1103,"name":"STAVANGER"}},"startTimeToday":null,"endTimeToday":null,"distanceFromClient":0,"tripAdvisorProduct":null,"externalSystemId":null,"externalSource":null,"searchResultScore":1}

## do later


class TrackEvent(db.Model):
    __tablename__ = 'trackevent'

    id = db.Column(db.INTEGER, primary_key=True)
    time = db.Column(db.DateTime, default=db.func.current_timestamp())
    temperature = db.Column(db.Float)
    rain = db.Column(db.Float)
    snow = db.Column(db.Float)
    weather = db.Column(db.Text(255))
    weatherdesc = db.Column(db.Text(255))
    rating = db.Column(db.INTEGER)  # 1 - 5, 0 = missing

    productid = db.Column(db.INTEGER, db.ForeignKey('product.id'))
    product = db.relationship(
        'Product', backref=db.backref(
            'trackevents', lazy='dynamic'))

    deviceid = db.Column(db.Text(255), db.ForeignKey('user.deviceid'))
    user = db.relationship(
        'User', backref=db.backref(
            'trackevents', lazy='dynamic'))

    def __init__(self, lat, long):
        weathertemp = json.dumps(getWeather(lat, long))
        self.temperature = weathertemp['temperature']
        self.snow = weathertemp['snow']
        self.rain = weathertemp['rain']
        self.weather = weathertemp['weather']
        self.weatherdesc = weathertemp['weatherdesc']

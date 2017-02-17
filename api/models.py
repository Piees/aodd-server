# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import MySQLdb
import config

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "mysql://" + config.user + ":" + config.password + "@" + config.database + "/" + config.schema
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    deviceid = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.Text(255))
    email = db.Column(db.Text(255))
    birthdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    sex = db.Column(db.Text(10))  # ho/han

    def __repr__(self):
        return "<User(deviceid={})>".format(self.deviceid)

    def __init__(self, deviceid):
        self.deviceid = deviceid

from flask import Flask
app = Flask(__name__)

import csv
import json

csvfilename = "testcsv.csv"
jsonfilename = csvfilename.split(0)[1].json


@app.route('/')
def welcome():
    return "this be the server boi"

@app.route('/events')
def events():

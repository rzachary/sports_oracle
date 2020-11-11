from flask import flask, jsonify, requests
from pymongo import MongoClient
import json
import csv

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/players', methods=['GET'])
def players():
    return "<h1>Function not complete: Get All The Players</h1>"


@app.route('/players/')


app.run()


from controllers import app
from flask import jsonify 
import pymongo
from pymongo import MongoClient


def get_db():
    client = MongoClient(host='for_mongodb_connection',
                         port=27017, 
                         username='Abraham', 
                         password='test-password',
                        authSource="admin")
    db = client["animal_db"]
    return db



@app.route("/")
def welcome():
    return "Hello Devoteam abraham"

@app.route("/members", methods = ['GET'])
def members():
    return jsonify({"members" : ["Member1", "Member2", "Member3"]})


@app.route('/animals') 
def fetch_animals () :
    db = get_db()
    _animals = db.animal_tb.find()
    animals = [{
        "id" : animal["id"],
        "name" : animal["name"],
        "type" : animal['type'],
    } for animal in _animals]
    
    return jsonify({"animals" : animals})

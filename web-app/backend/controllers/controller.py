from controllers import app
from flask import jsonify 

@app.route("/")
def welcome():
    return "Hello Devoteam"

@app.route("/members", methods = ['GET'])
def members():
    return jsonify({"members" : ["Member1", "Member2", "Member3"]})

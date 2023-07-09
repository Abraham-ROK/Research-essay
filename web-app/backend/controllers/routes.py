from controllers import app
from flask import request, jsonify, render_template, Blueprint, Flask
import pymongo
# from pymongo import MongoClient

# main=Blueprint("main", __name__)

# from bson.objectid import ObjectId



# def get_db():
#     client = MongoClient(host='for_mongodb_connection',
#                          port=27017, 
#                          username='mongo_user', 
#                          password='mongo_user_password',
#                         authSource="admin")
#     db = client["food_db"]
#     return db

client = pymongo.MongoClient("mongodb://mongo_user:mongo_user_password@Mongo_Database:27017/") # mongodb://mongo_user:mongo_user_password@Mongo_Database:27017/
                                                                                               # mongodb://localhost:27017/
db = client["testdb"]

@app.route("/")
def welcome():
    # return "Hello Devoteam abraham"
    return render_template("index.html")
    # return render_template("view.html")
    # return render_template("add.html")

@app.route("/foods", methods = ['POST', 'GET'])
def food_data():
    if request.method == 'POST':
        return render_template("add.html")
    elif request.method == 'GET':
        return render_template("view.html")

# @app.route("/members", methods = ['GET'])
# def members():
#     return jsonify({"members" : ["Member1", "Member2", "Member3"]})


@app.route("/users", methods = ['POST', 'GET'])

def data():
    if request.method == 'POST':
        body= request.json

        firstName = body["firstName"]
        lastName = body["lastName"]
        emailId = body["emailid"]
        db["users"].insert_one({
            "firstName": firstName,
            "lastName": lastName,
            "emailid": emailId
        })

        return jsonify({
            "status": "Data is posted to MongoDB",
            "firstName": firstName,
            "lastName":lastName,
            "emailid": emailId
        })
            


# {
#     "firstName": "John234",
#     "lastName": "Williamson234",
#     "emailid": "JohnWilliamso234@gmail.com"
# }
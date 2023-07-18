from controllers import app
from controllers.model import FOOD
from bson import ObjectId
import uuid
from controllers.database import get_db
from flask import request, jsonify, render_template, Blueprint, Flask
import pymongo
from datetime import datetime
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

# client = pymongo.MongoClient("mongodb://mongo_user:mongo_user_password@Mongo_Database:27017/") # mongodb://mongo_user:mongo_user_password@Mongo_Database:27017/
#                                                                                                # mongodb://localhost:27017/
# db = client["testdb"]

# def get_db():
#     mongo_db_client = pymongo.MongoClient("mongodb://mongo_user:mongo_user_password@Mongo_Database:27017/")
#     db = mongo_db_client["food_db"]
#     return db

# db = get_db()

@app.route("/home")
def welcome():
    # return render_template("index.html")
    # return render_template("view.html")
    return render_template("add.html")

@app.route("/foods", methods = ['POST', 'GET'])
def food_data():
    db = get_db()
    if request.method == 'POST':

        body= request.json

        food_id = str(uuid.uuid4())
        food = FOOD(body["Name"],body["Proteins"],body["Carbs"],body["Fats"],food_id)
        

        db["Foods"].insert_one({
            "Food_id": food.id,
            "Name": food.name,
            "Proteins": food.proteins,
            "Carbs": food.carbs,
            "Fats": food.fats,
            "Date": food.set_date,
            "Calories": food.set_calories
        })

        return jsonify({
            "status": "Data is posted to MongoDB",
            "Food_id": food.id,
            "Name": food.name,
            "Proteins": food.proteins,
            "Carbs": food.carbs,
            "Fats": food.fats,
            "Date": food.set_date,
            "Calories": food.set_calories
        })
    
        # return render_template("add.html")
    elif request.method == 'GET':

        all_food_data = db["Foods"].find()
        all_food_data_json =[]
        for data in all_food_data:
            food = FOOD(data["Name"], data["Proteins"],data["Carbs"],data["Fats"], data["Food_id"], data["Date"],data["Calories"])
            # id = data["_id"]

            food_data_dict = {
                # "Id" : str(id),
                "Food_id":food.id,
                "Name" : food.name,
                "Proteins" : food.proteins,
                "Carbs" : food.carbs,
                "Fats" : food.fats,
                "Date": food.insertion_date,
                "Calories": food.calories
            }

            all_food_data_json.append(food_data_dict)

        return jsonify(all_food_data_json)
        # return render_template("view.html")


@app.route("/foods/<string:id>", methods = ['PUT', 'GET', 'DELETE'])
def get_one_food_data(id):
    db = get_db()
    if request.method == 'GET':
        food_data = db["Foods"].find_one({"Food_id": id})   #({"_id":ObjectId(id)})
        # id = food_data["_id"]
        food = FOOD(
            food_data["Name"],
            food_data["Proteins"],
            food_data["Carbs"],
            food_data["Fats"],
            food_data["Food_id"],
            food_data["Date"],
            food_data["Calories"])
            

        food_data_dict = {
                # "Id" : str(id),
                "Food_id" : food.id,
                "Name" : food.name,
                "Proteins" : food.proteins,
                "Carbs" : food.carbs,
                "Fats" : food.fats,
                "Date": food.insertion_date,
                "Calories": food.calories
            }
        return jsonify(food_data_dict)
    elif request.method == 'DELETE':
        db["Foods"].delete_many({"Food_id": id})  #({"_id":ObjectId(id)})
        return jsonify({
            "status": "Data id: "+id+" is deleted"
        })
    elif request.method == 'PUT':
        body= request.json
        
        food = FOOD(body["Name"],body["Proteins"],body["Carbs"],body["Fats"])
  

        db["Foods"].update_one(
            # {"_id":ObjectId(id)},
            {"Food_id": id},
            {
                "$set":{
                    # "Food_id": food.set_id,
                    "Name": food.name,
                    "Proteins": food.proteins,
                    "Carbs": food.carbs,
                    "Fats": food.fats,
                    "Date": food.set_date,
                    "Calories": food.set_calories
                }
            }
        )
        return jsonify({
            "status": "Data id: "+id+" is updated"
        })

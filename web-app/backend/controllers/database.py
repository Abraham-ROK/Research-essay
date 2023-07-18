from controllers import app
import pymongo


def get_db():
    # mongo_db_client = pymongo.MongoClient("mongodb://mongo_user:mongo_user_password@Mongo_Database:27017/")
    mongo_db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = mongo_db_client["food_db"]
    
    return db
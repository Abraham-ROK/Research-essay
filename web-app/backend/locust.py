import time
from faker import Faker
import uuid
import random
import string
from bson.objectid import ObjectId

from controllers.model import FOOD


from locust import HttpUser, TaskSet, task, between

# class UserBehavior(TaskSet):
#     @task(1)
#     pass


fake = Faker()

class WebsiteUser(HttpUser):
    
    # def on_start(self):
    #     self.food_id = str(uuid.uuid4())  # Generate a unique ID for the user

    # tasks = [UserBehavior]
    wait_time = between(1, 5)

    @task(1)
    def food_page(self) :
        food_id = str(uuid.uuid4())
        food_test = FOOD(fake.word(),random.randint(5, 50),random.randint(5, 50),random.randint(5, 50),food_id)
        
        self.client.get(url="http://localhost:5001/foods") 
        self.client.post("http://localhost:5001/foods", json={  "Food_id": food_id,
                                                                "Name": food_test.name,
                                                                "Proteins": food_test.proteins,
                                                                "Carbs": food_test.carbs,
                                                                "Fats": food_test.fats
                                                                })
        # food_id = food_test.get_id
        self.client.get(f"http://localhost:5001/foods/food_id")
    
    
    # @task(2)
    # def get_food_data(self):
    #     food_test = FOOD(fake.word(),random.randint(5, 50),random.randint(5, 50),random.randint(5, 50))
    #     food_id = food_test.get_id  # Generate a random MongoDB-like _id
    #     self.client.get(f"http://localhost:5001/foods/{self.food_id}")

    # @task
    # def slow_page(self):
    #     self.client.get(url="/slow") locust -f locust.py --host http://localhost:5001/foods --users 5000 -- spawn-rate 50
    


    # locust -f locust.py --host=http://localhost:5001/foods --users=50 --spawn-rate=5 --run-time=1m --headless
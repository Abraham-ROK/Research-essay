import time
from faker import Faker
import random
import string


from locust import HttpUser, TaskSet, task, between

# class UserBehavior(TaskSet):
#     @task(1)
#     pass


fake = Faker()
class WebsiteUser(HttpUser):
    # tasks = [UserBehavior]
    wait_time = between(1, 5)


    @task
    def food_page(self) :
        self.client.get(url="http://localhost:5001/foods") 
        self.client.post("http://localhost:5001/foods", json={  "Name": fake.word(),
                                                                "Proteins": random.randint(5, 50),
                                                                "Carbs": random.randint(5, 50),
                                                                "Fats": random.randint(5, 50)})

    # @task
    # def slow_page(self):
    #     self.client.get(url="/slow") locust -f locust.py --host http://localhost:5001/foods --users 5000 -- spawn-rate 50
    


    # locust -f locust.py --host=http://localhost:5001/foods --users=50 --spawn-rate=5 --run-time=1m --headless
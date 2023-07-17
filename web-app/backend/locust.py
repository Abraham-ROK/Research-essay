import time

from locust import HttpUser, TaskSet, task, between

# class UserBehavior(TaskSet):
#     @task(1)
#     pass

class WebsiteUser(HttpUser):
    # tasks = [UserBehavior]
    wait_time = between(1, 5)


    @task
    def food_page(self) :
        self.client.get(url="http://localhost:5001/foods") 

    # @task
    # def slow_page(self):
    #     self.client.get(url="/slow") locust -f locust.py --host http://localhost:5001/foods --users 5000 -- spawn-rate 50
    
    # locust -f locust.py --host=http://localhost:5001/foods --users=50 --spawn-rate=5 --run-time=1m --headless
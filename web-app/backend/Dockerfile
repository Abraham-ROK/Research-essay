FROM python:3.9-alpine

# RUN mkdir -p workspace
WORKDIR /app


COPY requirements.txt requirements.txt

RUN 

RUN pip install --upgrade pip 
# RUN pip install pymongo

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

ENTRYPOINT [ "python", "server.py", "--reload"]

# CMD locust -f locust.py --host=http://localhost:5001/foods --users=50 --spawn-rate=5 --run-time=1m --headless
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

CMD [ "python", "server.py", "--reload"]
FROM python:3-alpine3.15

WORKDIR /app


COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD [ "python", "server.py" ]
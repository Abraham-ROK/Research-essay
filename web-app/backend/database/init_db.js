db = db.getSiblingDB("animal_db");
db.animal_tb.drop();

db.animal_tb.insertMany([
    {
        "id": 10,
        "name": "Lion",
        "type": "wild"
    },
    {
        "id": 2,
        "name": "Cow",
        "type": "domestic"
    },
    {
        "id": 3,
        "name": "Tiger",
        "type": "wild"
    },
]);
db = db.getSiblingDB("food_db");
db.food_tb.drop();

db.food_tb.insertMany([
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
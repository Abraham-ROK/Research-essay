from controllers import app

@app.route("/")
def welcome():
    return "Hello Devoteam"

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}
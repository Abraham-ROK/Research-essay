
from controllers import app


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5001)
    # app.run(debug=True,host="localhost", port=5001)



# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# if __name__ == "__main__":
    # app.run(debug=True,host="localhost", port=5001)
#     app.run(debug=True,host='0.0.0.0', port=5001)
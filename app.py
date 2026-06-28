print("The program started!")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello DevOps!</h1>"

app.run(debug=True)
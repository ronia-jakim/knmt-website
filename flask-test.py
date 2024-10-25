from flask import Flask

app = Flask(__name__)

@app.route("/build/")
def hello_world():
    return "<p>Hello, World!</p>"

from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "this be the server boi"

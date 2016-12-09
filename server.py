from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "this be the server boi"

@app.route('/events')
def getevents():
    return "no logic"

@app.route('/events', methods = ['POST'])
def postevents():
    return "no logic"

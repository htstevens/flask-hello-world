from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '0ad is the best game ever created!'

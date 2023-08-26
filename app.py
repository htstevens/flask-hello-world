from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'why did u search up this website?'

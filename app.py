
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Flask with docker!'
@app.route('/getgrades')
def home2():
    return 'Flask with docker 2.0!'

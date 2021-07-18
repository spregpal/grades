@from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Flask with docker!'
@app.route('/getgrades')
def getgrades():
    return 'Grade is 100!'

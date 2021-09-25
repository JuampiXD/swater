import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    responses = requests.get('https://75jwlvujpd.execute-api.us-east-2.amazonaws.com/staging/expeditions')
    expedition = eval(responses.text)
    return render_template('index.html', data=expedition)


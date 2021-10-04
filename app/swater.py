from Waterhole import Waterhole
import requests
from flask import Flask, render_template
from random import randrange

app = Flask(__name__)


@app.route("/")
def getInfo():
    responses = requests.get('https://75jwlvujpd.execute-api.us-east-2.amazonaws.com/staging/expeditions')
    info = eval(responses.text)
    water = Waterhole(info['x'],info['y'],info['tamano'])
    expedition = water.extractinfo()
    return render_template('index.html', expedition=expedition)
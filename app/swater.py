from Waterhole import Waterhole
import requests
from flask import Flask, render_template
import DataBase

app = Flask(__name__)


@app.route("/")
def getInfo():
    responses = requests.get('https://75jwlvujpd.execute-api.us-east-2.amazonaws.com/staging/expeditions')
    info = eval(responses.text)
    water = Waterhole(info['x'], info['y'], info['tamano'])
    expedition = water.extractinfo()
    database = DataBase.DataBase(expedition)
    database.Insert()
    return expedition

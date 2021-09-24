import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    responses = requests.get('https://75jwlvujpd.execute-api.us-east-2.amazonaws.com/staging/expeditions')
    expedition = eval(responses.text)
    message = "Sam dice  que vayas a: x:{}, y: {} el deposito tiene un tamaño de: {}".format(expedition['x'],
                                                                                             expedition['y'],
                                                                                             expedition['tamano'])
    return message

from random import randrange
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get():
    responses = requests.get('https://75jwlvujpd.execute-api.us-east-2.amazonaws.com/staging/expeditions')
    expedition = eval(responses.text)
    expedition['cheker'] = drinkable()
    return render_template('index.html', expedition=expedition)


def drinkable ():
    checker = randrange(2)
    print(checker)
    return checker


# def pull(*expedition):
#     return render_template('index.html', expedition=expedition)

import requests
from flask import Flask

app = Flask(__name__)

def vær(sted):
    url = f"https://wttr.in/{sted}?format=j1"
    respons = requests.get(url)
    data = respons.json()

    data['current_condition'][0]['FeelsLikeC'] # føles som
    værtype = data['current_condition'][0]['weatherDesc'][0]['value'] # værtypen
    temperatur = data['current_condition'][0]['temp_C'] # antall grader
    return værtype, temperatur


@app.get("/")
def hjem():
    return "Du må skrive et sted i adressefeltet. For eksempel: 127.0.0.1:5000/sandvika"

@app.get("/<string:sted>")
def rute_sted(sted: str):
    værtype, temperatur = vær(sted)
    return f"Været i {sted} er {værtype} og {temperatur} grader"

@app.get("/sandvika")
def rute_sandvika():
    værtype, temperatur = vær("sandvika")
    return f"I Sandvika er det {værtype} og {temperatur} grader"


app.run(debug=True)
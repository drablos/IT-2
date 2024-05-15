import json
import math
with open("sykkelturer.json") as fil:
    data_sykkelturer = json.load(fil)
startsted = {}
lengde = {}
distanse = {}

def regnlengde(hoyde, lengde):
    c = hoyde**2 + lengde**2
    return math.sqrt(c)


def presenter_data():
    for tur in data_sykkelturer:
        if tur["start_station_name"] in startsted:
            startsted[tur["start_station_name"]] += 1
        else:
            startsted[tur["start_station_name"]] = 1

        lengde[f"{tur["start_station_name"]} til {tur["end_station_name"]}"] = int(tur["duration"])

        distanse[f"{tur["start_station_name"]} til {tur["end_station_name"]}"] = regnlengde((float(tur["start_station_latitude"])- float(tur["end_station_latitude"])), (float(tur["start_station_longitude"])- float(tur["end_station_longitude"])) )

    startsted_sortert = sorted(startsted.items(), key=lambda tur:tur[1], reverse=True)
    lengde_sortert = sorted(lengde.items(), key=lambda tur:tur[1], reverse=True)
    distanse_sortert = sorted(distanse.items(), key=lambda tur:tur[1], reverse=True)

    print("--- Topp 5 stoppesteder ---")
    for i in range(0, 5):
        print(f"{i+1}. {startsted_sortert[i][0]}, med {startsted_sortert[i][1]} turer startet her")

    print("--- Topp 3 lengste turer, tid ---")
    for i in range(0, 3):
        print(f"{i+1}. {lengde_sortert[i][0]} på {lengde_sortert[i][1]} sekunder")

    print("--- Topp 3 lengste turer, distanse ---")
    for i in range(0, 3):
        print(f"{i+1}. {distanse_sortert[i][0]} på {distanse_sortert[i][1]} grader")



presenter_data()

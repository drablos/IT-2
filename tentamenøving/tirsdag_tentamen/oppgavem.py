def er_primtall(tall):
    for i in range(2, tall):
        if tall % i == 0:
            return True
    return False


def er_primtall(tall):
    """Sjekker om et gitt tall er et primtall.

    Args:
        tall (int): Tallet som skal sjekkes.

    Returns:
        bool: Returnerer True hvis tallet er et primtall, ellers False.

    Raises:
        ValueError: Hvis tallet er mindre enn eller lik 1.

    """
    if tall <= 1:
        raise ValueError("Tallet må være større enn 1 for å være et primtall.")

    for i in range(2, tall):
        if tall % i == 0:
            return False
    
    return True





# 1. Lag et program som presenterer de fem mest populare startstasjonene, og skriver ut navnet pá stasjonen og antall turer som startet der.
# 2. Utvid programmet slik at det ogsa presenterer de tre lengste turene (mält i tid), og skriver ut navnet pa start- og endestasjonen, samt turns varighet.
# 3. Utvid programmet slik at det ogsa presenterer de tre lengste turene (mält i distanse), og skriver ut navnet pá start- og endestasjonen.
# 1. Tips: Pytagoras, latitude og longitude.
# 2. Programmet trenger ikke presentere distansen.

trips = [
    {"start_station": "A", "end_station": "B", "duration_minutes": 30},
    {"start_station": "C", "end_station": "D", "duration_minutes": 45},
    {"start_station": "B", "end_station": "A", "duration_minutes": 40},
    {"start_station": "E", "end_station": "F", "distance_km": 20},  # Eksempel på turer med distanse (forenklet)
    {"start_station": "G", "end_station": "H", "distance_km": 25},
    # Legg til flere turer her etter behov
]

def find_most_popular_start_stations(trips, top_n=5):
    start_station_count = {}
    for trip in trips:
        start_station = trip["start_station"]
        if start_station in start_station_count:
            start_station_count[start_station] += 1
        else:
            start_station_count[start_station] = 1
    
    sorted_start_stations = sorted(start_station_count.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return sorted_start_stations

def find_longest_trips_by_duration(trips, top_n=3):
    sorted_trips_by_duration = sorted(trips, key=lambda x: x["duration_minutes"], reverse=True)[:top_n]
    return sorted_trips_by_duration

def find_longest_trips_by_distance(trips, top_n=3):
    trips_with_distance = [trip for trip in trips if "distance_km" in trip]
    sorted_trips_by_distance = sorted(trips_with_distance, key=lambda x: x["distance_km"], reverse=True)[:top_n]
    return sorted_trips_by_distance

# Funksjonen for å skrive ut resultatene
def print_results_most_popular_stations_and_longest_trips(trips):
    # 1. Finn de fem mest populære startstasjonene
    popular_start_stations = find_most_popular_start_stations(trips)
    print("De fem mest populære startstasjonene:")
    for station, count in popular_start_stations:
        print(f"{station}: {count} turer")

    print("\n")

    # 2. Finn de tre lengste turene målt i tid
    longest_trips_by_duration = find_longest_trips_by_duration(trips)
    print("De tre lengste turene målt i tid:")
    for trip in longest_trips_by_duration:
        print(f"Fra {trip['start_station']} til {trip['end_station']}, varighet: {trip['duration_minutes']} minutter")

    print("\n")

    # 3. Finn de tre lengste turene målt i distanse (forenklet)
    longest_trips_by_distance = find_longest_trips_by_distance(trips)
    print("De tre lengste turene målt i distanse (forenklet):")
    for trip in longest_trips_by_distance:
        print(f"Fra {trip['start_station']} til {trip['end_station']}")

# Kjør funksjonen for å skrive ut resultater
print_results_most_popular_stations_and_longest_trips(trips)





from collections import defaultdict
from datetime import datetime

# Kjøpsdata som gitt i oppgaven
kjopsdata = [
    {
        "kjopsdato": "2024-04-01",
        "posteringsdato": "2024-04-02",
        "beskrivelse": "TV2 A/S, BERGEN, NOR",
        "belop": "-398.00"
    },
    {
        "kjopsdato": "2024-03-30",
        "posteringsdato": "2024-04-02",
        "beskrivelse": "Vipps*Samtiden, Oslo, NOR",
        "belop": "-560.00"
    },
    {
        "kjopsdato": "2024-03-15",
        "posteringsdato": "2024-03-18",
        "beskrivelse": "Foodora Norway, Oslo, NOR",
        "belop": "-358.20"
    },
    # Legg til resten av kjøpsdataene her
]

# Dictionary for å holde oversikt over antall kjøp og tid mellom kjøp på hvert sted
sted_statistikk = defaultdict(lambda: {'antall_kjop': 0, 'tid_mellom_kjop': []})

# Gå gjennom hvert kjøp
for kjop in kjopsdata:
    beskrivelse = kjop['beskrivelse']
    kjopsdato = datetime.strptime(kjop['kjopsdato'], "%Y-%m-%d")
    
    # Oppdater antall kjøp på dette stedet
    sted_statistikk[beskrivelse]['antall_kjop'] += 1
    
    # Legg til tid mellom kjøp i listen (hvis det er mer enn ett kjøp på dette stedet)
    if sted_statistikk[beskrivelse]['antall_kjop'] > 1:
        for forrige_kjop in sted_statistikk[beskrivelse]['tid_mellom_kjop']:
            tid_mellom_kjop = (kjopsdato - forrige_kjop).days
            sted_statistikk[beskrivelse]['tid_mellom_kjop'].append(tid_mellom_kjop)
    
# Finn de 10 mest gjentatte stedene
top_10_steder = sorted(sted_statistikk.items(), key=lambda x: x[1]['antall_kjop'], reverse=True)[:10]

# Skriv ut resultatene
print("Top 10 steder med gjentatte kjøp:")
for sted, stats in top_10_steder:
    antall_kjop = stats['antall_kjop']
    tid_mellom_kjop_gjennomsnitt = sum(stats['tid_mellom_kjop']) / len(stats['tid_mellom_kjop']) if stats['tid_mellom_kjop'] else 0
    print(f"Sted: {sted}, Antall kjøp: {antall_kjop}, Gjennomsnittlig tid mellom kjøp: {tid_mellom_kjop_gjennomsnitt:.2f} dager")







# ny

from collections import defaultdict
from datetime import datetime

# Kjøpsdata som gitt i oppgaven
kjopsdata = [
    {
        "kjopsdato": "2024-04-01",
        "posteringsdato": "2024-04-02",
        "beskrivelse": "TV2 A/S, BERGEN, NOR",
        "belop": "-398.00"
    },
    {
        "kjopsdato": "2024-03-30",
        "posteringsdato": "2024-04-02",
        "beskrivelse": "Vipps*Samtiden, Oslo, NOR",
        "belop": "-560.00"
    },
    {
        "kjopsdato": "2024-03-15",
        "posteringsdato": "2024-03-18",
        "beskrivelse": "Foodora Norway, Oslo, NOR",
        "belop": "-358.20"
    },
    # Legg til resten av kjøpsdataene her
]

# Dictionary for å holde oversikt over antall kjøp og total pengebruk på hvert sted
sted_statistikk = defaultdict(lambda: {'antall_kjop': 0, 'total_pengebruk': 0})

# Gå gjennom hvert kjøp
for kjop in kjopsdata:
    beskrivelse = kjop['beskrivelse']
    belop = float(kjop['belop'])  # Konverter beløp til flyttall for beregninger
    
    # Oppdater antall kjøp og total pengebruk på dette stedet
    sted_statistikk[beskrivelse]['antall_kjop'] += 1
    sted_statistikk[beskrivelse]['total_pengebruk'] += belop

# Finn de 10 mest gjentatte stedene basert på antall kjøp
top_10_steder = sorted(sted_statistikk.items(), key=lambda x: x[1]['antall_kjop'], reverse=True)[:10]

# Skriv ut resultatene
print("Top 10 steder med gjentatte kjøp:")
for sted, stats in top_10_steder:
    antall_kjop = stats['antall_kjop']
    total_pengebruk = stats['total_pengebruk']
    
    print(f"Sted: {sted}")
    print(f"Antall kjøp: {antall_kjop}")
    print(f"Total pengebruk: {total_pengebruk:.2f} NOK")
    print("--------------------------")


from collections import defaultdict

# Kjøpsdata som gitt i oppgaven
kjopsdata = [
    {
        "kjopsdato": "2024-04-01",
        "posteringsdato": "2024-04-02",
        "beskrivelse": "TV2 A/S, BERGEN, NOR",
        "belop": "-398.00"
    },
    {
        "kjopsdato": "2024-03-30",
        "posteringsdato": "2024-04-02",
        "beskrivelse": "Vipps*Samtiden, Oslo, NOR",
        "belop": "-560.00"
    },
    {
        "kjopsdato": "2024-03-15",
        "posteringsdato": "2024-03-18",
        "beskrivelse": "Foodora Norway, Oslo, NOR",
        "belop": "-358.20"
    },
    # Legg til resten av kjøpsdataene her
]

# Dictionary for å holde oversikt over total pengebruk på hvert sted
sted_pengebruk = defaultdict(float)

# Gå gjennom hvert kjøp
for kjop in kjopsdata:
    beskrivelse = kjop['beskrivelse']
    belop = float(kjop['belop'])  # Konverter beløp til flyttall for beregninger
    
    # Oppdater total pengebruk for dette stedet
    sted_pengebruk[beskrivelse] += belop

# Finn de 10 stedene med høyest total pengebruk
top_10_steder = sorted(sted_pengebruk.items(), key=lambda x: x[1], reverse=True)[:10]

# Skriv ut resultatene
print("Top 10 steder med høyest total pengebruk:")
for sted, total_pengebruk in top_10_steder:
    print(f"Sted: {sted}")
    print(f"Total pengebruk: {total_pengebruk:.2f} NOK")
    print("--------------------------")





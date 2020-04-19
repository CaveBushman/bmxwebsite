import os
import csv
from datetime import date
import requests

from riders.models import Rider
from clubs.models import Club
from django.shortcuts import render, redirect, HttpResponse


def import_csv(request):
    print("Zahahuji převod")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file = os.path.join(BASE_DIR, '/vagrant/static/riders/csv/cze_riders.csv')
    print(BASE_DIR)
    print(csv_file)

    with open(csv_file) as f:
        readCSV = csv.reader(f, delimiter=',')
        data = list(readCSV)

        for row in data[1:len(data)]:
            new_rider = Rider()
            new_rider.uci_id = row[1]
            print(new_rider.uci_id)
            new_rider.first_name = row[8]
            new_rider.last_name = row[9].upper()
            if row[10] == "M":
                new_rider.gender = "Muž/Male"
            elif row[10] == "F":
                new_rider.gender = "Žena/Female"
            else:
                new_rider.gender = "Ostatní/Other"
            new_rider.plate = row[20]
            date_of_birth = row[7].replace('/', '-')
            new_rider.date_of_birth = date_of_birth
            new_rider.plate = row[20]
            new_rider.transponder_20 = row[29]
            new_rider.transponder_24 = row[30]
            new_rider.is_approwed = True
            if row[11] == "BMX &amp; 4X Team BRNO":
                row[11] = "BMX & 4X Team BRNO"
            if row[11] == "BMX &amp; 4X TEAM OLYMPUS":
                row[11] = "BMX & 4X TEAM OLYMPUS"
            club = row[11].upper()
            print(club)
            try:
                rider_club = Club.objects.get(name=club)
                new_rider.club = rider_club
            except:
                pass
            new_rider.is_challenge = row[14]
            new_rider.is_cruiser = row[15]
            new_rider.save()

    return HttpResponse('<h1>Jezdci převedeni</h1>')


def validation_licence(request):
    now = date.today()
    now = now.year

    basicAuthCredentials = ()

    riders = Rider.objects.all()

    for rider in riders:
        uci_id = rider.uci_id
        url_uciid = (f'https://data.ceskysvazcyklistiky.cz/licence-api/is-valid?uciId={uci_id}&year={now}')
        try:
            dataJSON = requests.get(url_uciid, auth=basicAuthCredentials)
            if dataJSON.text == "false" or dataJSON.status_code == 404:
                rider.have_valid_licence = False
                print(rider.last_name, " nemá platnou licenci")
                rider.save()
        except:
            pass

    return HttpResponse('<h1>ověření validity licencí skončilo</h1>')

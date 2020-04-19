import os
import csv
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

            club = row[11].upper()
            print(club)
            try:
                rider_club = Club.objects.get(name=club)
                new_rider.club = rider_club
            except:
                pass
            new_rider.save()

    return HttpResponse('<h1>Jezdci převedeni</h1>')

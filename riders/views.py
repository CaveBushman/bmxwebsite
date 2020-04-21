from django.shortcuts import render, redirect
from .models import Rider
from clubs.models import Club
from .forms import RiderForm
from .func import import_csv, validation_licence


# Create your views here.

def riders(request):
    if request.method == 'POST':
        pass
    else:
        riders = Rider.objects.filter(is_active="True")
        context = {"riders": riders}
        return render(request, 'riders/riders.html', context)


def plate_req(request):
    if request.method == 'POST':
        form = RiderForm(request.POST)
        if form.is_valid():
            print("Žádost o číslo - data validní")
            form.save()
        else:
            print("Data žádosti o číslo nejsou validní")
        return redirect('riders:riders')

    else:
        all_plates = []
        for plate in range(10, 1000):
            all_plates.append(plate)
        used_plates = []
        riders = Rider.objects.filter(is_active="True")
        for rider in riders:
            used_plates.append(rider.plate)
        for used_plate in used_plates:
            all_plates.remove(used_plate)  # ze všech čísel vymažu ty již obsazená aktivními jezdci
        print(all_plates)
        form = RiderForm()
        clubs = Club.objects.order_by('name')

        context = {'form': form, 'clubs': clubs, 'free_plates': all_plates}

        return render(request, 'riders/plate_req.html', context)

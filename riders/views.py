from django.shortcuts import render, redirect
from .models import Rider
from clubs.models import Club
from .forms import RiderForm
import requests


# Create your views here.

def riders(request):
    if request.method == 'POST':
        pass
    else:
        riders = Rider.objects.all()
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

        form = RiderForm()
        clubs = Club.objects.order_by('name')
        plates = (20, 21, 22, 23, 24)
        context = {'form': form, 'plates': plates, 'clubs':clubs}

        return render(request, 'riders/plate_req.html', context)

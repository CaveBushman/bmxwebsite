from django.shortcuts import render
from riders.models import Rider
from clubs.models import Club



# Create your views here.

def dashboards(request):
    riders = Rider.objects.filter(is_active=True).count()
    reqs_plate = Rider.objects.filter(is_approwed = False).count()
    clubs = Club.objects.filter(is_active = True).count()
    context = {'riders': riders, 'reqs_plate': reqs_plate, 'clubs': clubs}
    return render(request, 'dashboards/dashboards.html', context)

from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def clubs(request):
    if request == 'POST':
        pass
    else:
        clubs = Club.objects.order_by('name')
        context = {"clubs":clubs}
        return render(request, 'clubs/clubs.html', context)


def club_detail(request, pk):
    if request == 'POST':
        pass
    else:
        club = Club.objects.get(id=pk)
        context = {"club":club}
        return render(request, 'clubs/club_detail.html', context)

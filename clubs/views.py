from django.shortcuts import render, redirect


# Create your views here.

def clubs(request):
    if request == 'POST':
        pass
    else:
        context = {}
        return render(request, 'clubs/clubs.html', context)

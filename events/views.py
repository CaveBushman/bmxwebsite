from django.shortcuts import render
from .models import Event


# Create your views here.

def events(request):
    if request == 'POST':
        pass
    else:
        events = Event.objects.order_by('date', 'type')
        context = {'events': events}

        return render(request, 'events/events.html', context)

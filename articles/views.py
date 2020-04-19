from django.shortcuts import render
from riders.models import Rider
from clubs.models import Club
from events.models import Event
#from articles.models import Article
from datetime import date


# Create your views here.

def home(request):
    if request == 'POST':
        pass
    else:
        now = date.today()
        now = now.year

        riders = Rider.objects.filter(is_active=True).count()
        clubs = Club.objects.filter(is_active=True).count()
        events = Event.objects.filter(date__year=str(now)).count()
       # articles = Article.objects.all().count()

        context = {'riders': riders, 'clubs': clubs, 'events': events,}
        return render(request, 'articles/home.html', context)

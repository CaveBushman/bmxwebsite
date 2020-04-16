from django.contrib import admin
from .models import TranspondersForRental, Charge, Event
# Register your models here.

admin.site.register(Event)
admin.site.register(Charge)
admin.site.register(TranspondersForRental)

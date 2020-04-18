from django.contrib import admin
from .models import TranspondersForRental,  Event, Category, EventType, EventCategories
# Register your models here.

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(EventType)
admin.site.register(EventCategories)
admin.site.register(TranspondersForRental)

from django.db import models
from clubs.models import Club


# Create your models here.

class TranspondersForRental(models.Model):
    label = models.CharField(max_length=20, unique=True)
    transponder = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.label


class Charge(models.Model):
    name = models.CharField(max_length=255)

    challenge_online = models.IntegerField(null=True, blank=True)
    challenge_onspot = models.IntegerField(null=True, blank=True)

    cruiser_online = models.IntegerField(null=True, blank=True)
    cruiser_onspot = models.IntegerField(null=True, blank=True)

    junior_online = models.IntegerField(null=True, blank=True)
    junior_onspot = models.IntegerField(null=True, blank=True)

    elite_online = models.IntegerField(null=True, blank=True)
    elite_onspot = models.IntegerField(null=True, blank=True)

    mtb_online = models.IntegerField(null=True, blank=True)
    mtb_onspot = models.IntegerField(null=True, blank=True)

    other_online = models.IntegerField(null=True, blank=True)
    other_onspot = models.IntegerField(null=True, blank=True)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=50)
    

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    ranking_code = models.CharField(max_length=50, blank=True, null=True)

    organizer = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)

    charge = models.ForeignKey(Charge, on_delete=models.SET_NULL, null=True)

    is_challenge = models.BooleanField(default=True)
    is_cruiser = models.BooleanField(default=True)
    is_junior = models.BooleanField(default=True)
    is_elite = models.BooleanField(default=True)
    is_mtb = models.BooleanField(default=False)
    is_other = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

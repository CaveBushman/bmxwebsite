from django.db import models
from clubs.models import Club


# Create your models here.

class TranspondersForRental(models.Model):
    label = models.CharField(max_length=20, unique=True)
    transponder = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.label


class EventType(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=50)
    age_from = models.IntegerField()
    age_to = models.IntegerField()

    def __str__(self):
        return self.name


class EventCategories(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    type = models.ForeignKey(

        EventType,
        on_delete=models.CASCADE,
    )
    charge_online = models.IntegerField()
    charge_onspot = models.IntegerField()

    is_valid = models.BooleanField(default=True)

    def __str__(self):
        full_return = self.type.name + " - " + self.category.name
        return (full_return)


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)

    type = models.ForeignKey(
        EventType,
        on_delete=models.CASCADE
    )
    ranking_code = models.CharField(max_length=50, blank=True, null=True)

    organizer = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)

    is_canceled = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

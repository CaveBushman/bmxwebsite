from django.db import models
from events.models import Event
from riders.models import Rider


# Create your models here.

class RankingData(models.Model):
    rider = models.ForeignKey(
        Rider,
        on_delete=models.CASCADE,
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    place = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        full_label = str(self.event.date) + ", " + self.event.name + ", UCI ID: " + self.rider.uci_id + ", " + self.rider.last_name + " " + self.rider.first_name
        return full_label

from django.db import models
from clubs.models import Club


# Create your models here.

class Rider(models.Model):
    GENDER = (('Muž/Male', 'Muž/Male'), ('Žena/Female', 'Žena/Female'), ('Ostatní/Other', 'Ostatní/Other'))

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)

    uci_id = models.CharField(max_length=255, unique=True)

    gender = models.CharField(max_length=50, default='M', choices=GENDER)

    email = models.EmailField(blank=True, null=True)

    club = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)

    plate = models.IntegerField()
    plate_2 = models.IntegerField(null=True, blank=True)

    transponder_20 = models.CharField(max_length=10, null=True, blank=True)
    transponder_24 = models.CharField(max_length=10, null=True, blank=True)
    transponder_mtb = models.CharField(max_length=10, null=True, blank=True)
    transponder_other = models.CharField(max_length=10, null=True, blank=True)

    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    emergency_phone = models.CharField(max_length=255, null=True, blank=True)

    is_challenge = models.BooleanField(default=True)
    is_elite = models.BooleanField(default=False)
    is_cruiser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_approwed = models.BooleanField(default=False)

    have_valid_licence = models.BooleanField(default=True)

    path_to_photo = models.CharField(max_length=255, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        full_name = self.last_name + " " + self.first_name + " UCI ID: " + self.uci_id
        return full_name

    def count(self):
        pass

    def lastNameUppercase(self):
        return self.last_name.upper()

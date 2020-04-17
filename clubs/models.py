from django.db import models


# Create your models here.

class Club(models.Model):
    REGION = (
        ('Praha', 'Praha'), ('Středočeský', 'Středočeský'), ('Západočeský', 'Západočeský'), ('Jihočeský', 'Jihočeský'),
        ('Ústecký', 'Ústecký'), ('Plzeňský', 'Plzeňský'), ('Karlovarský', 'Karlovarský'),
        ('Liberecký', 'Liberecký'), ('Parbubický', 'Parbubický'), ('Královéhradecký', 'Královéhradecký'),
        ('Vysočina', 'Vysočina'), ('Jihomoravský', 'Jihomoravský'), ('Moravskoslezský', 'Moravskoslezský'),
        ('Olomoucký', 'Olomoucký'), ('Zlínský', 'Zlínský'),)
    name = models.CharField(max_length=200, null=True, unique=True)
    company_number = models.CharField(max_length=50, null=True, blank=True)

    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    post_no = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=255, null=True, choices=REGION)

    web = models.URLField(null=True, blank=True)
    contact_person = models.CharField(max_length=255, null=True, blank=True)
    contact_phone = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)

    bank_account = models.CharField(max_length=255, null=True, blank=True)
    bank_code = models.CharField(max_length=100, null=True, blank=True)
    swift = models.CharField(max_length=255, null=True, blank=True)
    iban = models.CharField(max_length=255, null=True, blank=True)

    paypal_id = models.CharField(max_length=255, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

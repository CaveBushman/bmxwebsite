from django.forms import ModelForm
from .models import Rider


class RiderForm(ModelForm):
    class Meta:
        model = Rider
        exclude = ('is_approwed','is_active',)

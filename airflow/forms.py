from django.forms import ModelForm
from .models import *


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

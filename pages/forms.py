from django import forms
from .models import Deceased

class DeceasedForm(forms.ModelForm):
    class Meta:
        model = Deceased
        fields = ('first_name', 'last_name', 'gender', 'birthdate', 'birth_city', 'birth_state',
        'birth_country', 'deathdate', 'death_city', 'death_state', 'death_country','bio' )

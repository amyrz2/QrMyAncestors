from django import forms
from .models import Biography

class BiographyForm(forms.ModelForm):
    class Meta:
        model = Biography
        fields = ('first_name', 'last_name', 'gender', 'birth_day', 'birth_city', 'birth_state',
        'birth_country', 'death_day', 'death_city', 'death_state', 'death_country','bio' )

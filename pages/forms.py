from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Deceased



# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=True)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class DeceasedForm(forms.ModelForm):
    class Meta:
        model = Deceased
        fields = ('first_name', 'last_name', 'gender', 'birthdate', 'birth_city', 'birth_state',
        'birth_country', 'deathdate', 'death_city', 'death_state', 'death_country','bio' )

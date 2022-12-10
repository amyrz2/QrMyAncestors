from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
#Change your models (in models.py).
#Run python manage.py makemigrations to create migrations for those changes
#Run python manage.py migrate to apply those changes to the database.


class Deceased(models.Model):
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    deceased_first_name = models.CharField(max_length=30)
    deceased_last_name = models.CharField(max_length=30)
    deceased_gender = models.CharField(max_length=1)
    deceased_birth_date= models.DateField(help_text= "Deceased's birthday")
    deceased_birth_city = models.CharField(max_length=30)
    deceased_birth_state = models.CharField(max_length=30)
    deceased_birth_country = models.CharField(max_length=30)
    deceased_death_date= models.DateField(help_text= "Deceased's deathday")
    deceased_death_city = models.CharField(max_length=30)
    deceased_death_state = models.CharField(max_length=30)
    deceased_death_country = models.CharField(max_length=30)
    deceased_biography = models.CharField(max_length=20000)


    @property
    def deceased_full_name(self):
        return '%s %s' % (self.deceased_first_name, self.deceased_last_name)
    
    def __str__(self):
        return (self.deceased_full_name)


   

from django.db import models
from django.utils import timezone
# Create your models here.
#Change your models (in models.py).
#Run python manage.py makemigrations to create migrations for those changes
#Run python manage.py migrate to apply those changes to the database.


class User(models.Model):
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=50)
    user_login = models.CharField(max_length=30)
    user_password = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=10) 

    @property
    def user_full_name(self):
        return '%s %s' % (self.user_first_name, self.user_last_name)
    
    def __str__(self):
        return (self.user_full_name)

class Deceased(models.Model):
    user = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL)
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

class Biography(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=15)
    birth_day = models.DateField()
    birth_city = models.CharField(max_length=50)
    birth_state = models.CharField(max_length=50)
    birth_country = models.CharField(max_length=50)
    death_day = models.DateField()
    death_city = models.CharField(max_length=50)
    death_state = models.CharField(max_length=50)
    death_country = models.CharField(max_length=50)
    bio = models.TextField()


   

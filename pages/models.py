from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=50)
#     login = models.CharField(max_length=30)
#     password = models.CharField(max_length=20)
#     phone = models.CharField(max_length=10) 
#     class Meta:
#         db_table = 'user'
    
#     def __str__(self):
#         return f'{self.first_name, self.last_name, self.email, self.login, self.password, self.phone}'

class Deceased(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    birthdate = models.DateField()
    birth_city = models.CharField(max_length=30)
    birth_state = models.CharField(max_length=30)
    birth_country = models.CharField(max_length=30)
    deathdate= models.DateField()
    death_city = models.CharField(max_length=30)
    death_state = models.CharField(max_length=30)
    death_country = models.CharField(max_length=30)
    bio = models.TextField()

    objects = models.Manager()
    class Meta:
        db_table = 'deceased'

    
    def __str__(self):
        return f'{self.first_name, self.last_name, self.gender, self.birthdate, self.birth_city, self.birth_state, self.birth_country, self.deathdate, self.death_city, self.death_state, self.death_country}'





   

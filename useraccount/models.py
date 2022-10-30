from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
#Change your models (in models.py).
#Run python manage.py makemigrations to create migrations for those changes
#Run python manage.py migrate to apply those changes to the database.


class User(models.Model):
    user_email = models.CharField(max_length=50, primary_key=True)
    user_username = models.CharField(max_length=200)
    user_fname = models.CharField(max_length=16)
    user_lname = models.CharField(max_length=16)
    user_created_on = timezone.now()
    def __str__(self):
        return self.user_username


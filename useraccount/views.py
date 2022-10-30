from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import User
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'useraccount/index.html'
    context_object_name = 'user_account_list'

    def get_queryset(self):
        return User.objects.filter(user_email = 'wirickad@gmail.com')


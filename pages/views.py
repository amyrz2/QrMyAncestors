# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Biography
from .forms import BiographyForm
#from django.views import generic

from .models import User
# Create your views here.

def indexPageView(request) :
    return render(request, 'pages/index.html') 
 
def aboutPageView(request) :
    return render(request, 'pages/about.html')

def loginPageView(request) :
    return render(request, 'pages/login.html')

def communityPageView(request) :
    return render(request, 'pages/community.html')

def ancestorsPageView(request) :
    return render(request, 'pages/ancestors.html')

def createaccountPageView(request) :
    return render(request, 'pages/createAccount.html')

def biographyPageView(request):
    if request.method == 'POST':
        form = BiographyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/index.html') 
    else:
        form = BiographyForm()
    return render(request, 'pages/biography.html', {'form': form})


    
""" def profilePageView(request, person_name) :
    sOutput='<html>'\
                '<head><title>Contact</title></head>'\
                '<body>'\
                    '<p style="font-size:50px; color:white; background-color:#779ecb; text-align:center;">About ' + person_name + '\'s Story</p>'\
                '</body>'\
            '</html>'
    return HttpResponse(sOutput) """

#class IndexView(generic.ListView):
    #template_name = 'pages/index.html'
    #context_object_name = 'user_account_list'

    #This is a query that will send the desired user's information to the html page
    #def get_queryset(self):
        #return User.objects.filter(user_email = 'wirickad@gmail.com')
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect  
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Deceased
from .forms import DeceasedForm
#from django.views import generic

from .models import User
#from django.views import generic


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

# View to display the form for creating a new biography profile
def bio_create_view(request):
    form = DeceasedForm()
    if request.method == 'POST':
        form = DeceasedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bioView/')
    context = {
        'form': form
    }
    return render(request, 'pages/bioCreate.html', context)

# View to handle the submission of the form and create a new biography profile in the database
def bio_list_view(request):
    biographies = Deceased.objects.all()
    context = {
        'biographies': biographies
    }
    return render(request, 'pages/bioList.html', context)

# View to display the form for updating an existing biography profile
def bio_update_view(request, pk):
    biography = Deceased.objects.get(pk=pk)
    form = DeceasedForm(instance=biography)
    if request.method == 'POST':
        form = DeceasedForm(request.POST, instance=biography)
        if form.is_valid():
            form.save()
            return redirect('/bioView/')
    context = {
        'form': form
    }
    return render(request, 'pages/bioUpdate.html', context)

# View to handle the submission of the form and update the existing biography profile in the database
def bio_delete_view(request, pk):
    biography = Deceased.objects.get(pk=pk)
    if request.method == 'POST':
        biography.delete()
        return redirect('/bioView/')
    context = {
        'biography': biography
    }
    return render(request, 'pages/bioDelete.html', context)
    


#class IndexView(generic.ListView):
    #template_name = 'pages/index.html'
    #context_object_name = 'user_account_list'

    #This is a query that will send the desired user's information to the html page
    #def get_queryset(self):
        #return User.objects.filter(user_email = 'wirickad@gmail.com')
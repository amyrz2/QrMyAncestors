# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect  
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Deceased
from .forms import DeceasedForm
#from django.views import generic
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import User


# create class views here
class CreateDeceased(CreateView):
    form_class = DeceasedForm
    template_name = 'pages/deceasedForm.html'

    def form_valid(self, form):
        deceased = form.save(commit=False)
        deceased.created_by = self.request.user
        deceased.save()
        return redirect('pages/deceasedDetail.html', deceased.id)

class DeseasedDetail(DetailView):
    model = Deceased
    context_object_name = 'deceased'
    template_name = 'pages/deceasedDetail.html'

class ListDeceased(ListView):
    model = Deceased
    template_name = 'pages/deceasedList.html'

class UpdateDeceased(UpdateView):
    form_class = DeceasedForm
    model = Deceased
    template_name = 'pages/deceasedForm.html'

class DeleteDeceased(DeleteView):
    model = Deceased
    success_url = '/deceased/'
    template_name = 'pages/deceasedConfirmDelete.html'

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
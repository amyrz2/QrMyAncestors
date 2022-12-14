# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect  
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
import qrcode
from PIL import Image
from .models import Deceased
from .forms import DeceasedForm
from django.contrib.auth.models import User
#from django.views import generic

#if request.user.is_authenticated:
    # Do something for authenticated users.
    
#else:
    # Do something for anonymous users.
    

#from django.views import generic


# Create your views here.

def indexPageView(request) :
    return render(request, 'pages/index.html') 
 
def aboutPageView(request) :
    return render(request, 'pages/about.html')

def loginPageView(request) :
    
    if request.method == "POST":
        sUsername = request.POST['usn']
        sPassword = request.POST['psw']
        user = authenticate(request, username=sUsername, password=sPassword)
        if user is not None:
            
            login(request, user)
            # Redirect to a success page.
            response = HttpResponseRedirect('/bioView/')
            return response
            
        else:
            print("Failed")
            context = {'failed':True}
            return render(request, 'pages/login.html',context)
    else:
        return render(request, 'pages/login.html')

# View to display the form for creating a new biography profile
def bio_create_view(request):
    form = DeceasedForm()
    if request.method == 'POST':
        f = DeceasedForm(request.POST)
        if f.is_valid():
            print(request.user.id)
            new_bio = f.save(commit=False)
            new_bio.user_id = request.user.id
            new_bio.save()
            return redirect('/bioView/')
    context = {
        'form': form
    }
    return render(request, 'pages/bioCreate.html', context)

# View to handle the submission of the form and create a new biography profile in the database
def bio_list_view(request):
    thisUser = request.user.id
    
    #entries = Journal_Line_Item.objects.filter(user=thisUser)
    biographies = Deceased.objects.filter(user_id = thisUser)
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
        'biography' : biography
    }
    
    return render(request, 'pages/bioDelete.html', context)
    
def showSingleProfile(request, pk):
    biography = Deceased.objects.get(pk=pk)
   
    context = {
        'biography' : biography
    }
    return render(request, 'pages/viewonebio.html', context) 

def qr_code(request):
    url = request.build_absolute_uri()
    img = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def logout_view(request):
    logout(request)
    return redirect('/')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Registration successful." )
            return redirect('/login/')
        else:
            print('failed')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, "pages/register.html", context={"register_form":form})


# def bio_create_view(request):
#     form = DeceasedForm()
#     if request.method == 'POST':
#         form = DeceasedForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/bioView/')
#     context = {
#         'form': form
#     }
#     return render(request, 'pages/bioCreate.html', context)

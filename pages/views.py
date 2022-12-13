# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
import qrcode
from PIL import Image
#from django.views import generic

#if request.user.is_authenticated:
    # Do something for authenticated users.
    
#else:
    # Do something for anonymous users.
    

# Create your views here.

def indexPageView(request) :
    return render(request, 'pages/index.html') 
 
def aboutPageView(request) :
    return render(request, 'pages/about.html')

def loginPageView(request) :
    if request.method == "GET":
        return render(request, 'pages/login.html')
    else:
        sUsername = request.POST['usn']
        sPassword = request.POST['psw']
        user = authenticate(request, username=sUsername, password=sPassword)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            response = HttpResponseRedirect('/')
            return response
            
        else:
            context = {'failed':True}
            return render(request, 'pages/login.html',context)

def communityPageView(request) :
    return render(request, 'pages/community.html')

def ancestorsPageView(request) :
    return render(request, 'pages/ancestors.html')


def qr_code(request):
    url = request.build_absolute_uri()
    img = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

def logout_view(request):
    logout(request)
    return redirect('/')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return HttpResponseRedirect('/')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, "pages/register.html", context={"register_form":form})


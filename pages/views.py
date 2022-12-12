# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
import qrcode
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

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "pages/register.html", context={"register_form":form})

# def createaccountPageView(request) :
#     return render(request, 'pages/createAccount.html')
# """ def profilePageView(request, person_name) :
#     sOutput='<html>'\
#                 '<head><title>Contact</title></head>'\
#                 '<body>'\
#                     '<p style="font-size:50px; color:white; background-color:#779ecb; text-align:center;">About ' + person_name + '\'s Story</p>'\
#                 '</body>'\
#             '</html>'
#     return HttpResponse(sOutput) """

def qr_code(request):
    url = request.build_absolute_uri()
    img = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    
    
    return response


from django.urls import path
from .views import indexPageView, aboutPageView, profilePageView
# if you use this -> from . import views 
# then you just do views.viewname in urlpattern path('', views.IndexView.as_view(), name='index'),


urlpatterns = [
    path("", indexPageView, name="index") ,    
    path("about/", aboutPageView, name="about"),    
    path("profile/<str:person_name>", profilePageView, name="profile")
]  

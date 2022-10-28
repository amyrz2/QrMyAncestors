from django.urls import path
from .views import indexPageView, aboutPageView, profilePageView


urlpatterns = [
    path("", indexPageView, name="index") ,    
    path("about", aboutPageView, name="about"),    
    path("profile/<str:person_name>", profilePageView, name="profile")
]  

from django.urls import path
from . import views #use this, and then just do views.viewname
# if you use this -> from . import views 
# then you just do views.viewname in urlpattern path('', views.IndexView.as_view(), name='index'),

app_name = 'pages'
urlpatterns = [
    path('', views.indexPageView, name='index'),   
    path("about/", views.aboutPageView, name="about"),    
    path("profile/<str:person_name>", views.profilePageView, name="profile")
]  

#Ignore the line below for now
#path('<int:pk>/', views.DetailView.as_view(), name='detail'),

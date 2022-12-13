from django.urls import path
from . import views #use this, and then just do views.viewname


# if you use this -> from . import views 
# then you just do views.viewname in urlpattern path('', views.IndexView.as_view(), name='index'),

app_name = 'pages'
urlpatterns = [
    path('', views.indexPageView, name='index'),   
    path("about/", views.aboutPageView, name="about"),    
    path("login/", views.loginPageView, name="login"), 
    path("community/", views.communityPageView, name="community"),
    path("ancestors/", views.ancestorsPageView, name="ancestors"),
    path("register/", views.register_request, name='register'),
    path("logout/",views.logout_view,name='logout'),
    path("generate_qr/",views.qr_code, name='generate_qr'),
    path('bioCreate/', views.bio_create_view, name='bio-create'),
    path('bioView/', views.bio_list_view, name='biophy-list'),
    path('<int:pk>/bioUpdate/', views.bio_update_view, name='bio-update'),
    path('<int:pk>/bioDelete/', views.bio_delete_view, name='bio-delete'),
    
    #path("profile/<str:person_name>", views.profilePageView, name="profile")
]  

#Ignore the line below for now
#path('<int:pk>/', views.DetailView.as_view(), name='detail'),

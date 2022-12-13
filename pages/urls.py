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
    path("createAccount/", views.createaccountPageView, name="createAccount"),
    path('deceased/new/', views.CreateDeceased.as_view(), name='deceased_create'),
    path('deceased/<int:pk>/edit/', views.UpdateDeceased.as_view(), name='deceased_edit'),
    path('deceased/<int:pk>/delete/', views.DeleteDeceased.as_view(), name='deceased_delete'),
    path('deceased/list', views.ListDeceased.as_view(), name='deceased_list'),
    path('deceased/detail', views.DeseasedDetail.as_view(), name='deceased_detail'),
    #path("profile/<str:person_name>", views.profilePageView, name="profile")
]  

#Ignore the line below for now
#path('<int:pk>/', views.DetailView.as_view(), name='detail'),

from django.urls import path

from . import views #use this, and then just do views.viewname

app_name = 'useraccount'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
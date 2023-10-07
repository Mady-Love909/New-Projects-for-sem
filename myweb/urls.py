from django.urls import path
from myweb import views

urlpatterns = [
    path('',views.welcome,name="welcome"),
    path('home',views.home,name="home"),
    path('loginform',views.loginform,name="loginform"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('infocomp',views.infocomp,name="infocomp"),
    path('signin',views.signin,name="signin"),
    path('google',views.google,name="google"),
    path('apple',views.apple,name="apple"),
    path('ibm',views.ibm,name="ibm"),
    path('details',views.details,name="details"),
    
]



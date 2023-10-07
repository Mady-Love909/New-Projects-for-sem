from django.urls import path
from myweb import views

urlpatterns = [
    path('',views.home,name="home"),
    path('loginform',views.loginform,name="loginform"),
    path('contacts',views.contacts,name="contacts"),
]



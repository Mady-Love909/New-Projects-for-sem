from django.contrib import admin
from django.urls import path
from msgymmain import views
urlpatterns = [
    
    path('',views.index,name="index"),

]
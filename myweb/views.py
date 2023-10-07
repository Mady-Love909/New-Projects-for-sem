from django.shortcuts import render
from myweb.models import Dbcontact


# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def home(request):
    return render(request,'homepage.html')

def loginform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        address = request.POST.get('address')
    
        city = request.POST.get('city')

        state = request.POST.get('state')

        zip = request.POST.get('zip')
        mname = request.POST.get('mname')
        login = Dbcontact(name = name , lname = lname, email = email, password = password, address = address, city = city, state = state, zip = zip,mname = mname)
        login.save()        

    return render(request,'loginform.html')

def aboutus(request):
    return render(request,'aboutus.html')

def infocomp(request):
    return render(request,'company.html')

def signin(request):
    return render(request,'signin.html')


def google(request):
    return render(request,'google.html')

def apple(request):
    return render(request,'apple.html')

def ibm(request):
    return render(request,'ibm.html')

def details(request):
    return render(request,'details.html')






 


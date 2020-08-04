from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World!!</h1>")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

def showpage(request):
    return render(request, "myfirstapp/index.html")

def getdata(request, name):
    return render(request, 'myfirstapp/getdata.html',{
        'name' : name
    })

def newyear(request):
    now = datetime.datetime.utcnow()
    return render(request, 'myfirstapp/newyear.html',{
        'newyear' : now.month == 1 and now.day == 1
    })
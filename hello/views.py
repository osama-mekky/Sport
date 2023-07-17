from django.http import HttpResponse
from django.shortcuts import render
 
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def mekky(request):
    return render(request,"index.html")

def login(request):
    return render(request,'login.html')
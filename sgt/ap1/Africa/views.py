from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "lin.html")

def Senegal(request):
     return render(request, "Senegal.html")

def Guine(request):
     return render(request, "Guine.html")


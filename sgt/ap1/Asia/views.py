from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     return render(request, "links.html")

def India(request):
     return render(request, "India.html")

def Japão(request):
     return render(request, "Japão.html")

def Coreiadosul(request):
     return render(request, "Coreiadosul.html")
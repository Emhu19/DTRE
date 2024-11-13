from django.shortcuts import render

from webapp.models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact (request):
    return render(request,'contact.html')

def doc(request):
    return render(request,'documentation.html',{'documentations':Documentation.objects.all()})

def events(request):
    return render(request,'evenements.html',{'events':Event.objects.all()})

def member(request):
    return render(request, 'membres.html',{'membres':Membre.objects.all()})

def project(request):
    return render(request, 'projets.html',{'projets':Projet.objects.all()})


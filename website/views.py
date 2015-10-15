from django.shortcuts import render

# Create your views here.
from website.models import Gallery


def home(request):
    return render(request, "home.html", {'nav_id': 'home'})

def galerie(request):
    galleries = Gallery.objects.all()
    return render(request, "galerie.html",
                  {
                      'nav_id': 'galerie',
                      'galleries': galleries
                  }
                  )

def prestation(request):
    return render(request, "prestation.html", {'nav_id': 'prestation'})

def map(request):
    return render(request, "map.html", {'nav_id': 'map'})
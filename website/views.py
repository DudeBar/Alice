import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from website.models import Gallery, Images


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

def get_photos(request, gallery_id):
    images = Images.objects.filter(gallery=gallery_id)
    images_urls = {}
    cpt = 0
    for image in images:
        images_urls[cpt] = image.photo.url
        cpt += 1
    response = JsonResponse(images_urls)
    return response

def prestation(request):
    return render(request, "prestation.html", {'nav_id': 'prestation'})

def map(request):
    return render(request, "map.html", {'nav_id': 'map'})
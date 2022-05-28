from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pin, Location, category


# Create your views here.

def homepage(request):
    title='Pin your Interests'
    images=Pin.display_pins()
    return render (request,'all-pages/index.html', {"title":title, "images":images})

def search_pin_by_category(request):
    title={{images.pin_name}}
    images=Pin.search_pin_by_category()
    return render(request, "all-pages/search.html",{"title":title, "images":images})

def search_pin_by_location(request):
    images=Pin.search_pin_by_location()
    title={{images.pin_name}}
    return render(request,'all-pages/search-by-location.html',{"title":title,"images":images})
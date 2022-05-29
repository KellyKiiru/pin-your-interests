from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Pin, Location, category
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def homepage(request):
    title='Pin your Interests'
    images=Pin.display_pins()
    locations = Location.objects.all()
    return render (request,'all-pages/index.html', {"title":title, "images":images, "locations":locations})

def show_single_pin(request, pin_id):
    try:
        pin = Pin.objects.get(id = pin_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-pages/pin.html", {"pin":pin})

def search_pin_by_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Pin.search_by_category(search_term)
        message = f'{search_term}'
        
        return render(request,'all-pages/search.html',{"pins":searched_images,"category":search_term,"message":message})
    
def search_pin_by_location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    pins = Pin.objects.filter(location = selected_location.id)
    return render(request, 'all-pages/location.html', {"location":selected_location,"locations":locations,"pins":pins})
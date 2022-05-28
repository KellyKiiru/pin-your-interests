from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Pin, Location, category
from django.core.exceptions import ObjectDoesNotExist


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

def show_single_pin(request, pin_id):
    try:
        pin = Pin.objects.get(id = pin_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-pages/pin.html", {"pin":pin})

def search_results(request):
    if 'pin' in request.GET and request.GET['pin']:
        search_term = request.GET.get('pin')
        searched_pin = Pin.search_by_title(search_term)
        message = f'{search_term}'
        
        return render(request,'all-pages/search.html',{"message": message,"pin":searched_pin,"search_term":search_term})
    else:
        message= "You haven't searched for any term"
        return render(request,'all-pages/search.html',{"message":message})
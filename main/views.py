from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def homepage(request):
    title='Pin your Interests'
    return render (request,'index.html', {"title":title})


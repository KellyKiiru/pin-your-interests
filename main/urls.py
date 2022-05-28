from . import views
from django.urls import path

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('location/<pin_id>/',views.search_pin_by_location, name='search_pin_by_location'),
    path('category/<pin_id>',views.search_pin_by_category,name='search_pin_by_location'),    
]
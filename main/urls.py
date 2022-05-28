from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('location/<pin_id>/',views.search_pin_by_location, name='search_pin_by_location'),
    path('category/<pin_id>',views.search_pin_by_category,name='search_pin_by_location'),    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

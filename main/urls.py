from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('pin/<int:pin_id>',views.show_single_pin, name='show_single_pin'),
    path('location/<pin_id>/',views.search_pin_by_location, name='search_pin_by_location'),
    path('category/<pin_id>',views.search_pin_by_category,name='search_pin_by_location'),
    path('search/', views.search_results,name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

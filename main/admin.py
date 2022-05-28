from django.contrib import admin
from .models import category,Location,Pin

# Register your models here.

admin.site.register(Pin)
admin.site.register(Location)
admin.site.register(category)

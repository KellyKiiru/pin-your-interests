from django.contrib import admin
from .models import category,Location,Pin
# Register your models here.

class PinAdmin(admin.ModelAdmin):
    filter_horizontal=('category',)

admin.site.register(Pin,PinAdmin)
admin.site.register(Location)
admin.site.register(category)

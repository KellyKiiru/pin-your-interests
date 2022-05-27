from enum import unique
from django.db import models


# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=40)
    location_list=[]
    
    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save()
    

class category(models.Model):
    category_name=models.CharField(max_length=40)
    category_list=[]
    
    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save()

class Pin(models.Model):
    pin_name=models.CharField(max_length=30)
    pin_description=models.CharField(max_length=100)
    category=models.ManyToManyField(category)
    pin_image=models.ImageField(upload_to='pins/', unique=True)
    
    def save_pin(self):
        self.save()
        
    class Meta:
        ordering = ['pin_name']
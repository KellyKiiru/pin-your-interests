from django.db import models


# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=40)
    location_list=[]
    
    
    def save_location(self):
        self.save()
        
    def __str__(self):
        return self.location
    
    

class category(models.Model):
    category_name=models.CharField(max_length=40,unique=False, blank=False)
    category_list=[]
    
    def save_category(self):
        self.save()
        
    def __str__(self):
        return self.category_name
    

class Pin(models.Model):
    pin_name=models.CharField(max_length=30)
    pin_description=models.TextField()
    category=models.ManyToManyField(category)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    pin_image=models.ImageField(upload_to='pins/', unique=True)
            
    class Meta:
        ordering = ['pin_name']
    
    def save_pin(self):
        self.save()
        
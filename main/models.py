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
    category=models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True)
   
    pin_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    pin_image=models.ImageField(upload_to='pins/', unique=True)
            
    class Meta:
        ordering = ['pin_name']
    
    def save_pin(self):
        self.save()
        
    @classmethod
    def display_pins(cls):
        images=cls.objects.all()
        return images 
    
    @classmethod
    def search_pin_by_category(cls,category):
        images=cls.objects.filter(category__ic=category)
        return images
    @classmethod
    def search_pin_by_location(cls,pin_location):
        images= cls.objects.filter(location__icontains=pin_location)
        return images
    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
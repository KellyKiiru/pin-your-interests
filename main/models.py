from django.db import models

# Create your models here.

class Pin(models.Model):
    pin_name=models.CharField(max_length=30)
    pin_description=models.CharField(max_length=100)
    pin_image=models.ImageField(upload_to='pins/')
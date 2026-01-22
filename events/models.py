from django.db import models

class FunctionType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='function_images/')
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='venue_images/')
    
    def __str__(self):
        return self.name

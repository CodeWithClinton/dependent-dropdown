from sre_parse import Verbose
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=15)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
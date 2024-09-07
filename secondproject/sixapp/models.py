from django.db import models

# Create your models here.
class ModelName(models.Model): #id
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=50)
    
    def __str__(self):
        return self.field1
    

class Book(models.Model): #id
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=50)
    Written_by = models.CharField(max_length=40)
    
    def __str__(self):
        return self.Name



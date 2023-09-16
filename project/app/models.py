from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    message=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

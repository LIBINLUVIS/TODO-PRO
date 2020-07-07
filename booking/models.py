from django.db import models

# Create your models here.


class booking(models.Model):

    first_name=models.TextField(max_length=50)
    second_name=models.TextField(max_length=50)
    place = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    
    


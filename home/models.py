from django.db import models

# Create your models here.

class destination(models.Model):
   
   place = models.TextField()
   price = models.IntegerField()
   img = models.ImageField(upload_to='pics')



   












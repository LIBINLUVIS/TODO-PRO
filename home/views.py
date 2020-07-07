from django.shortcuts import render,redirect
from . models import destination
from django.contrib.auth.models import User,auth


# Create your views here.

def index(request):
  
   dests=destination.objects.all()
       
   return render(request,"index.html",{'dests':dests})

def london(request):
   return render (request,"learnlondon.html")

      
      
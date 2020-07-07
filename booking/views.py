from django.shortcuts import render,redirect
from . models import booking
from django.contrib import messages

# Create your views here.

def booknow(request):

    if request.method == 'POST':
        first_name=request.POST["first_name"]
        second_name=request.POST["second_name"]
        place =request.POST["place"]
        email = request.POST["email"]
        book_now=booking(first_name=first_name,second_name=second_name,place=place,email=email)
        book_now.save();
        return redirect("/")
        

    else:
        return render(request,'booknow.html')
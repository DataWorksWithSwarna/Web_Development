from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from firstapp.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        # Process the form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number")
        concerns = request.POST.get("concerns")

        # Create a new Contact instance
        contact = Contact(
            name=name,
            email=email,
            contact_number=contact_number,
            concerns=concerns
        )
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
    return render(request, "contact.html")

def products(request):
    return render(request, "products.html")

def loginuser(request):
    if request.method == "POST":

        #Process the login form data
        Username = request.POST.get("username")
        password = request.POST.get("password")

        # Here you would typically authenticate the user using Django's authentication system
        user = authenticate(request, username=Username, password=password) 

        # For demonstration, we'll just check if the username and password are not empty
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home page after successful login
        else:
            messages.error(request, "Please enter both username and password.")
            #return render(request, "login.html")
    
    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("home")

def user_checkout(request):
    return render(request, "checkout.html")
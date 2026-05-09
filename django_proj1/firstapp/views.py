from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from datetime import datetime
from firstapp.models import Contact, Product, Cart
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

def user_products(request):
    return render(request, "user_products.html")

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

    cart = request.session.get('cart', {})

    total = 0

    for key, item in cart.items():

        item['subtotal'] = item['price'] * item['quantity']

        total += item['subtotal']

    context = {
        'cart': cart,
        'total': total
    }
    return render(request, "checkout.html")

def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, "details.html", {
        'product': product
    })

def cart(request):
    cart_items = Cart.objects.all()

    total = 0

    for item in cart_items:
      item.subtotal = item.product.price * item.quantity
      total += item.subtotal

    return render(request, "cart.html", {
        'cart_items': cart_items,
        'total': total
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    
    cart_item, created = Cart.objects.get_or_create(
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")

def clear_cart(request):

    Cart.objects.all().delete()

    return redirect("cart")

#def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect("cart")

#def update_cart(request, product_id):

    if request.method == "POST":

        quantity = int(request.POST.get('quantity'))

        cart = request.session.get('cart', {})

        product_id = str(product_id)

        if product_id in cart:

            if quantity > 0:
                cart[product_id]['quantity'] = quantity
            else:
                del cart[product_id]

        request.session['cart'] = cart

    return redirect("cart")